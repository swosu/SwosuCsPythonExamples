import os, csv, json, zipfile
from collections import OrderedDict
from pathlib import Path

root = Path.cwd()
outdir = root / "ch12_outputs"
outdir.mkdir(exist_ok=True)

def ensure_file(path, content):
    if not path.exists():
        path.write_text(content, encoding="utf-8")

words_file = outdir / "input1.txt"
ensure_file(words_file, "\n".join([
    "aspiration","classified","federation","graduation","millennium",
    "philosophy","quadratics","transcript","wilderness","zoologists"
]) + "\n")

lower = "ammoniated"
upper = "millennium"
with words_file.open("r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]
range_results = [f"{w} - {'in range' if lower <= w <= upper else 'not in range'}" for w in words]
(outdir / "range_results.txt").write_text("\n".join(range_results) + "\n", encoding="utf-8")
(outdir / "range_results.json").write_text(json.dumps(
    [{"word": w, "status": ("in" if lower <= w <= upper else "out")} for w in words],
    ensure_ascii=False, indent=2
), encoding="utf-8")

csv_file = outdir / "input1.csv"
ensure_file(csv_file, "hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy")
counts = OrderedDict()
with csv_file.open("r", encoding="utf-8", newline="") as f:
    for row in csv.reader(f):
        for tok in row:
            w = tok.strip()
            if not w:
                continue
            counts[w] = counts.get(w, 0) + 1
freq_lines = [f"{w} - {c}" for w, c in counts.items()]
(outdir / "frequencies.txt").write_text("\n".join(freq_lines) + "\n", encoding="utf-8")
(outdir / "frequencies.json").write_text(json.dumps(counts, ensure_ascii=False, indent=2), encoding="utf-8")

tv_file = outdir / "file1.txt"
ensure_file(tv_file, "\n".join([
    "20","Gunsmoke","30","The Simpsons","10","Will & Grace",
    "14","Dallas","20","Law & Order","12","Murder, She Wrote"
]) + "\n")
with tv_file.open("r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
shows_by_seasons = {}
for i in range(0, len(lines), 2):
    k = int(lines[i])
    v = lines[i + 1]
    shows_by_seasons.setdefault(k, []).append(v)
with (outdir / "output_keys.txt").open("w", encoding="utf-8") as outk:
    for k in sorted(shows_by_seasons.keys(), reverse=True):
        outk.write(f"{k}: {'; '.join(shows_by_seasons[k])}\n")
all_titles = []
for v in shows_by_seasons.values():
    all_titles.extend(v)
with (outdir / "output_titles.txt").open("w", encoding="utf-8") as outt:
    for title in sorted(all_titles, reverse=True):
        outt.write(f"{title}\n")
(outdir / "tv_shows.json").write_text(json.dumps(shows_by_seasons, ensure_ascii=False, indent=2), encoding="utf-8")

tsv_file = outdir / "StudentInfo.tsv"
ensure_file(tsv_file, "\n".join([
    "Barrett\tEdan\t70\t45\t59",
    "Bradshaw\tReagan\t96\t97\t88",
    "Charlton\tCaius\t73\t94\t80",
    "Mayo\tTyrese\t88\t61\t36",
    "Stern\tBrenda\t90\t86\t45"
]) + "\n")

def letter(x):
    if x >= 90: return "A"
    if x >= 80: return "B"
    if x >= 70: return "C"
    if x >= 60: return "D"
    return "F"

students = []
m1_sum = m2_sum = fin_sum = 0
with tsv_file.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if len(row) < 5:
            continue
        last, first = row[0], row[1]
        m1, m2, fin = int(row[2]), int(row[3]), int(row[4])
        avg = (m1 + m2 + fin) / 3
        grade = letter(avg)
        students.append((last, first, m1, m2, fin, grade))
        m1_sum += m1
        m2_sum += m2
        fin_sum += fin
n = len(students)
m1_avg = m1_sum / n if n else 0.0
m2_avg = m2_sum / n if n else 0.0
fin_avg = fin_sum / n if n else 0.0
with (outdir / "report.txt").open("w", encoding="utf-8", newline="") as out:
    for s in students:
        out.write(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\n")
    out.write("\n")
    out.write(f"Averages: midterm1 {m1_avg:.2f}, midterm2 {m2_avg:.2f}, final {fin_avg:.2f}\n")
grade_dist = {}
for s in students:
    grade_dist[s[5]] = grade_dist.get(s[5], 0) + 1
(outdir / "grades.json").write_text(json.dumps({
    "students": [{"last": s[0], "first": s[1], "midterm1": s[2], "midterm2": s[3], "final": s[4], "letter": s[5]} for s in students],
    "averages": {"midterm1": round(m1_avg, 2), "midterm2": round(m2_avg, 2), "final": round(fin_avg, 2)},
    "distribution": grade_dist
}, ensure_ascii=False, indent=2), encoding="utf-8")

index_html = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Chapter 12 — Cool Suite</title>
<style>
body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;max-width:900px;margin:40px auto;padding:0 16px;line-height:1.5}}
h1{{margin-bottom:0}}
small{{color:#666}}
section{{border:1px solid #ddd;border-radius:12px;padding:16px;margin:16px 0}}
code,a{{font-family:ui-monospace,Menlo,Consolas,monospace}}
ul{{margin:8px 0 0 18px}}
.badge{{display:inline-block;background:#111;color:#fff;border-radius:999px;padding:2px 10px;font-size:12px;margin-left:8px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.card{{border:1px solid #eee;border-radius:10px;padding:12px}}
</style>
</head>
<body>
<h1>Chapter 12 — Cool Suite <span class="badge">Auto-Generated</span></h1>
<small>All inputs created if missing. Outputs linked below.</small>
<section>
<h2>12.8 Words in a Range</h2>
<div class="grid">
<div class="card"><b>Input</b><br><code>{words_file.name}</code></div>
<div class="card"><b>Output</b><br><a href="./{(outdir/'range_results.txt').name}">range_results.txt</a> · <a href="./{(outdir/'range_results.json').name}">range_results.json</a></div>
</div>
<ul>{"".join(f"<li>{line}</li>" for line in range_results[:5])}{'<li>…</li>' if len(range_results)>5 else ''}</ul>
</section>
<section>
<h2>12.9 Word Frequencies</h2>
<div class="grid">
<div class="card"><b>Input</b><br><code>{csv_file.name}</code></div>
<div class="card"><b>Output</b><br><a href="./{(outdir/'frequencies.txt').name}">frequencies.txt</a> · <a href="./{(outdir/'frequencies.json').name}">frequencies.json</a></div>
</div>
<ul>{"".join(f"<li>{w} — {c}</li>" for w,c in list(counts.items())[:6])}{'<li>…</li>' if len(counts)>6 else ''}</ul>
</section>
<section>
<h2>12.10 Sorting TV Shows</h2>
<div class="grid">
<div class="card"><b>Input</b><br><code>{tv_file.name}</code></div>
<div class="card"><b>Output</b><br><a href="./{(outdir/'output_keys.txt').name}">output_keys.txt</a> · <a href="./{(outdir/'output_titles.txt').name}">output_titles.txt</a> · <a href="./{(outdir/'tv_shows.json').name}">tv_shows.json</a></div>
</div>
<ul>{"".join(f"<li>{k}: {'; '.join(v)}</li>" for k,v in sorted(shows_by_seasons.items(), reverse=True))}</ul>
</section>
<section>
<h2>12.11 Course Grade</h2>
<div class="grid">
<div class="card"><b>Input</b><br><code>{tsv_file.name}</code></div>
<div class="card"><b>Output</b><br><a href="./{(outdir/'report.txt').name}">report.txt</a> · <a href="./{(outdir/'grades.json').name}">grades.json</a></div>
</div>
<ul>{"".join(f"<li>{s[0]} {s[1]} — {s[2]}, {s[3]}, {s[4]} → {s[5]}</li>" for s in students)}</ul>
<p><b>Averages:</b> midterm1 {m1_avg:.2f}, midterm2 {m2_avg:.2f}, final {fin_avg:.2f}</p>
</section>
</body>
</html>
"""
(outdir / "index.html").write_text(index_html, encoding="utf-8")

with zipfile.ZipFile(outdir / "ch12_bundle.zip", "w", compression=zipfile.ZIP_DEFLATED) as z:
    for p in outdir.iterdir():
        if p.is_file() and p.name != "ch12_bundle.zip":
            z.write(p, arcname=p.name)

print("Created outputs in", outdir.as_posix())
for p in sorted(outdir.iterdir()):
    if p.is_file():
        print("-", p.name)
