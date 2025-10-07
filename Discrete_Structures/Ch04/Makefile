# ===============================================
# Makefile — Discrete Structures: Section 4.6 (Cryptography)
# Auto-compiles all .tex files → PDFs and merges them
# Keeps source + PDFs; cleans only temp build files
# Auto-detects merge tool (pdftk or pdfunite)
# ===============================================

LATEX=pdflatex
OUT=student_worksheets.pdf

# Detect available merge tool (pdftk preferred, fallback to pdfunite)
MERGE := $(shell command -v pdftk 2>/dev/null || command -v pdfunite 2>/dev/null)
MERGE_IS_PDFTK := $(findstring pdftk,$(MERGE))

# Gather all LaTeX sources and expected PDF outputs
TEX_FILES := $(wildcard *.tex)
PDF_FILES := $(TEX_FILES:.tex=.pdf)

# -----------------------------------------------
# Default target
# -----------------------------------------------
all: $(OUT)

# -----------------------------------------------
# Compile individual LaTeX files into PDFs
# -----------------------------------------------
%.pdf: %.tex
	@echo "🧩 Compiling $< ..."
	@$(LATEX) -interaction=nonstopmode $< >/dev/null || echo "⚠️  Warnings occurred in $< (PDF likely still generated)."

# -----------------------------------------------
# Merge all PDFs alphabetically into one document
# -----------------------------------------------
$(OUT): $(PDF_FILES)
	@echo "📚 Found merge tool: $(MERGE)"
	@echo "📘 Combining $(words $(PDF_FILES)) PDF(s) into $(OUT) ..."
ifeq ($(MERGE_IS_PDFTK),pdftk)
	@$(MERGE) $(sort $(PDF_FILES)) cat output $(OUT)
else
	@$(MERGE) $(sort $(PDF_FILES)) $(OUT)
endif
	@echo "✅ Build complete! Combined file created: $(OUT)"

# -----------------------------------------------
# Cleanup utilities
# -----------------------------------------------
clean:
	@echo "🧹 Cleaning LaTeX auxiliary files (logs kept for debugging)..."
	@rm -f *.aux *.log *.out *.toc *.synctex.gz

cleanall: clean
	@echo "🧼 Removing all intermediate build files (PDFs kept)."
	@rm -f temp.* *.bak

# -----------------------------------------------
# Full rebuild from scratch
# -----------------------------------------------
rebuild: clean all

.PHONY: all clean cleanall rebuild

