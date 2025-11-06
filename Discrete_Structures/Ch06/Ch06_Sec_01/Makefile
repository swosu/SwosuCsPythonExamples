# --- COMSC 2043: Counting Workbook Build Script (Rocky 9 edition) ---
# Builds LaTeX documents cleanly and safely on Rocky / Linux

# Default target
all: pdf

# --- Variables ---
MAIN  := main
LATEX := pdflatex -interaction=nonstopmode -halt-on-error
BIB   := bibtex
SRC   := $(MAIN).tex
PDF   := $(MAIN).pdf

# --- Build PDF (with references) ---
pdf:
	@echo "🧠 Compiling LaTeX..."
	@$(LATEX) $(SRC)
	@if [ -f "$(MAIN).aux" ]; then $(BIB) $(MAIN) || true; fi
	@$(LATEX) $(SRC)
	@$(LATEX) $(SRC)
	@echo "✅ Build complete: $(PDF)"

# --- View PDF ---
view:
	@echo "👀 Opening PDF..."
	@if command -v xdg-open >/dev/null 2>&1; then \
		xdg-open $(PDF) >/dev/null 2>&1 & \
	else \
		echo "⚠️  'xdg-open' not found. Please open $(PDF) manually."; \
	fi

# --- Clean up intermediate files ---
clean:
	@echo "🧹 Cleaning up LaTeX build files..."
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.lof *.lot *.fls *.fdb_latexmk
	rm -f $(PDF)

# --- Rebuild from scratch ---
rebuild: clean pdf

# --- Run Python experiments (optional) ---
run:
	@echo "🐍 Running Python experiments (if any)..."
	@if [ -f scripts/run_experiments.py ]; then \
		python3 scripts/run_experiments.py; \
	else \
		echo "No experiments found."; \
	fi

