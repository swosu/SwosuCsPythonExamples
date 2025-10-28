# --- COMSC 2043 Induction & Recursion Student Workbook ---
# Automates code execution and LaTeX build

PY_SCRIPTS = chapters/fib_bench.py chapters/fib_memprobe.py chapters/big_o_plot.py

# Default target: run Python experiments and build LaTeX
all: run pdf

# Run all analyses
run:
	@echo "🚀 Running analysis scripts..."
	@for s in $(PY_SCRIPTS); do \
		echo "[OK] Executing $$s"; \
		python3 $$s || exit 1; \
	done

# Compile LaTeX (2 passes for references)
pdf:
	pdflatex main.tex
	bibtex main.aux || true
	pdflatex main.tex
	pdflatex main.tex

clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.lof *.lot *.fls *.fdb_latexmk

# Optional shortcut: force rebuild everything
rebuild: clean all

