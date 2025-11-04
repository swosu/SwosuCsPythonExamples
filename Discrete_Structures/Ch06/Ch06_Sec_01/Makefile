# --- COMSC 2043: Counting Workbook Build Script ---
# Builds LaTeX documents cleanly and safely on Windows or Linux

# Default target
all: pdf

# Detect OS and choose the right open command
ifeq ($(OS),Windows_NT)
	OPEN = start
else
	OPEN = xdg-open
endif

# --- Variables ---
MAIN = main
LATEX = pdflatex -interaction=nonstopmode -halt-on-error
BIB   = bibtex
SRC   = $(MAIN).tex
PDF   = $(MAIN).pdf

# --- Build PDF (with references) ---
pdf:
	@echo "🧠 Compiling LaTeX..."
	$(LATEX) $(SRC)
	@if [ -f "$(MAIN).aux" ]; then $(BIB) $(MAIN).aux || true; fi
	$(LATEX) $(SRC)
	$(LATEX) $(SRC)
	@echo "✅ Build complete: $(PDF)"

# --- View PDF (cross-platform) ---
view:
	@echo "👀 Opening PDF..."
	$(OPEN) $(PDF)

# --- Clean up intermediate files ---
clean:
	@echo "🧹 Cleaning up LaTeX build files..."
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.lof *.lot *.fls *.fdb_latexmk
	rm -f $(PDF)

# --- Rebuild from scratch ---
rebuild: clean pdf

# --- Run Python experiments (if needed later) ---
run:
	@echo "🐍 Running Python experiments (if any)..."
	@if [ -f scripts/run_experiments.py ]; then python scripts/run_experiments.py; else echo "No experiments found."; fi
