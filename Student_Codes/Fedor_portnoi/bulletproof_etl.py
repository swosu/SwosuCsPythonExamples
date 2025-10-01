#!/usr/bin/env python3
import argparse, csv, json, logging, os, random, sqlite3, sys, time
from datetime import datetime
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

class ETLError(Exception): ...
class NetworkError(ETLError): ...
class ParseError(ETLError): ...
class ValidationError(ETLError): ...
class DatabaseError(ETLError): ...

def backoff_sleep(i, base=0.3, cap=2.0):
    time.sleep(min(cap, base * (2 ** i) + random.random() * 0.1))

def is_url(path):
    try:
        return bool(urlparse(path).scheme in ("http", "https", "file"))
    except Exception:
        return False

def read_source(path_or_url, timeout=5, attempts=3):
    if is_url(path_or_url):
        last = None
        for i in range(attempts):
            try:
                req = Request(path_or_url, headers={"User-Agent":"bulletproof-etl/1.0"})
                with urlopen(req, timeout=timeout) as r:
                    data = r.read()
                    return data
            except HTTPError as e:
                if 500 <= e.code < 600 and i < attempts - 1:
                    backoff_sleep(i)
                    last = e
                    continue
                raise NetworkError(f"http error {e.code}: {path_or_url}") from e
            except URLError as e:
                if i < attempts - 1:
                    backoff_sleep(i)
                    last = e
                    continue
                raise NetworkError(f"url error: {path_or_url}") from e
            except Exception as e:
                if i < attempts - 1:
                    backoff_sleep(i)
                    last = e
                    continue
                raise NetworkError(f"network read failed: {path_or_url}") from e
        raise NetworkError(f"unreachable: {path_or_url}") from last
    else:
        try:
            with open(path_or_url, "rb") as f:
                return f.read()
        except FileNotFoundError as e:
            raise NetworkError(f"file not found: {path_or_url}") from e
        except PermissionError as e:
            raise NetworkError(f"permission denied: {path_or_url}") from e
        except OSError as e:
            raise NetworkError(f"io error: {path_or_url}") from e

def to_int(v):
    return int(v)

def to_email(v):
    return str(v).strip().lower()

def to_amount(v):
    x = float(v)
    if x < 0:
        raise ValueError("negative")
    return round(x, 2)

def to_ts(v):
    return datetime.fromisoformat(str(v))

SCHEMA = {"id": to_int, "email": to_email, "amount": to_amount, "created_at": to_ts}

def validate_row(row):
    out = {}
    for k, fn in SCHEMA.items():
        if k not in row or row[k] in (None, "", []):
            raise ValidationError(f"missing {k}")
        try:
            out[k] = fn(row[k])
        except Exception as e:
            raise ValidationError(f"bad {k}") from e
    return out

def iter_rows_csv(text):
    try:
        for row in csv.DictReader(text.splitlines()):
            yield row
    except Exception as e:
        raise ParseError("csv parse error") from e

def iter_rows_jsonl(text):
    for ln, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            if not isinstance(obj, dict):
                raise ValueError("not an object")
            yield obj
        except Exception as e:
            raise ParseError(f"jsonl parse error on line {ln}") from e

def write_sqlite(rows, db_path, upsert=False):
    try:
        os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    except Exception:
        pass
    try:
        with sqlite3.connect(db_path, timeout=2) as db:
            db.execute("""CREATE TABLE IF NOT EXISTS records(
                id INTEGER PRIMARY KEY,
                email TEXT NOT NULL,
                amount REAL NOT NULL,
                created_at TEXT NOT NULL
            )""")
            if upsert:
                sql = ("INSERT INTO records(id,email,amount,created_at) VALUES(?,?,?,?) "
                       "ON CONFLICT(id) DO UPDATE SET email=excluded.email, amount=excluded.amount, created_at=excluded.created_at")
            else:
                sql = "INSERT INTO records(id,email,amount,created_at) VALUES(?,?,?,?)"
            db.executemany(sql, rows)
    except sqlite3.OperationalError as e:
        raise DatabaseError("db operational error (locked or schema issue)") from e
    except sqlite3.IntegrityError as e:
        raise DatabaseError("db integrity error (unique/constraint)") from e

def process_source(source, fmt, failures_dir, db_path, upsert=False):
    ok = 0
    bad = 0
    base = os.path.basename(urlparse(source).path) or "source"
    fail_path = os.path.join(failures_dir, f"{base}.log")
    os.makedirs(failures_dir, exist_ok=True)
    try:
        raw = read_source(source)
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            try:
                text = raw.decode("cp1251")
            except UnicodeDecodeError as e:
                raise ParseError("unable to decode (utf-8, cp1251)") from e
        rows_iter = iter_rows_csv(text) if fmt == "csv" else iter_rows_jsonl(text)
        good = []
        failed_lines = []
        for row in rows_iter:
            try:
                clean = validate_row(row)
                good.append((clean["id"], clean["email"], clean["amount"], clean["created_at"].isoformat()))
            except ValidationError as e:
                bad += 1
                failed_lines.append(f"validation\t{str(e)}\t{row}\n")
        if good:
            write_sqlite(good, db_path, upsert=upsert)
            ok += len(good)
        if failed_lines:
            with open(fail_path, "a", encoding="utf-8") as f:
                for line in failed_lines:
                    f.write(line)
        return ok, bad
    except (NetworkError, ParseError, DatabaseError) as e:
        logging.exception(f"fatal for {source}")
        raise

def parse_args():
    p = argparse.ArgumentParser(description="Bulletproof Mini-ETL (one-file)")
    p.add_argument("--inputs", nargs="+", required=True, help="URLs or local file paths")
    p.add_argument("--format", choices=["csv","jsonl"], required=True, help="Input format")
    p.add_argument("--out", required=True, help="SQLite database path")
    p.add_argument("--upsert", action="store_true", help="Upsert rows on duplicate id")
    p.add_argument("--failures-dir", default="failures", help="Where to write failure logs")
    return p.parse_args()

def main():
    args = parse_args()
    total_ok = 0
    total_bad = 0
    for src in args.inputs:
        try:
            ok, bad = process_source(src, args.format, args.failures_dir, args.out, upsert=args.upsert)
            total_ok += ok
            total_bad += bad
            logging.info(f"{src}: ok={ok} bad={bad}")
        except ETLError:
            return 1
    if total_ok > 0 and total_bad > 0:
        return 2
    return 0

if __name__ == "__main__":
    sys.exit(main())
