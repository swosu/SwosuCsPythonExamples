# ===============================================
# Makefile for Section 4.6 — Cryptography
# Auto-builds all .tex -> .pdf and merges results
# Keeps .tex + .pdf, cleans up all other junk
# ===============================================

LATEX=pdflatex
MERGE=pdftk
OUT=student_worksheets.pdf

# Collect all .tex files automatically
TEX_FILES := $(wildcard *.tex)
PDF_FILES := $(TEX_FILES:.tex=.pdf)

# -----------------------------------------------
# Default target
# -----------------------------------------------
all: $(OUT)

# Compile each .tex file individually
%.pdf: %.tex
	@echo "🧩 Compiling $< ..."
	@$(LATEX) -interaction=nonstopmode $< >/dev/null

# Merge all PDFs in alphanumeric order
$(OUT): $(PDF_FILES)
	@echo "📚 Merging PDFs into $(OUT) ..."
	@$(MERGE) $(sort $(PDF_FILES)) cat output $(OUT)
	@echo "✅ Build complete! Combined file: $(OUT)"

# -----------------------------------------------
# Cleanup targets
# -----------------------------------------------
clean:
	@echo "🧹 Cleaning auxiliary LaTeX files ..."
	@rm -f *.aux *.log *.out *.toc *.synctex.gz

# Leave PDFs intact; remove only junk files
cleanall: clean
	@echo "✨ Clean complete (PDFs retained)."

# -----------------------------------------------
# Utility: rebuild everything from scratch
# -----------------------------------------------
rebuild: clean all

.PHONY: all clean cleanall rebuild

