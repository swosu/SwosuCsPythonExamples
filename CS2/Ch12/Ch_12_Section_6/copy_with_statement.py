src = "input.txt"
dst = "copy.txt"
with open(src, "r", encoding="utf-8") as inp, open(dst, "w", encoding="utf-8") as out:
    for line in inp:
        out.write(line)
print(f"Copied {src} → {dst}")

