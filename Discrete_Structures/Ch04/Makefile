# ===============================================
# Makefile — Discrete Structures: Section 4.6 Cryptography
# Auto-compiles all .tex files -> PDFs and merges them
# Keeps source + PDFs; cleans only temp build files
# Auto-detects merge tool (pdftk or pdfunite)
# ===============================================

LATEX=pdflatex
OUT=student_worksheets.pdf

# Auto-detect merge tool (pdftk preferred, fallback to pdfunite)
MERGE := $(shell command -v pdftk 2>/dev/null || command -v pdfunite 2>/dev/null)
MERGE_IS_PDFTK := $(findstring pdftk,$(MERGE))

# Gather LaTeX sources and PDFs
TEX_FILES := $(wildcard *.tex)
PDF_FILES := $(TEX_FILES:.tex=.pdf)

# -----------------------------------------------
# Default target
# -----------------------------------------------
all: $(OUT)

# Compile each .tex to .pdf, stop gracefully on error
%.pdf: %.tex
	@echo "🧩 Compiling $< ..."
	@if ! $(LATEX) -interaction=nonstopmode $< >/dev/null; then \
	  echo "❌ LaTeX error in $< — check $*.log for details"; \
	  tail -n 10 $*.log || true; \
	  exit 1; \
	fi

# Merge all generated PDFs alphabetically
$(OUT): $(PDF_FILES)
	@echo "📚 Found merge tool: $(MERGE)"
	@echo "📘 Combining $(words $(PDF_FILES)) PDF(s) into $(OUT) ..."
ifeq ($(MERGE_IS_PDFTK),pdftk)
	@$(MERGE) $(sort $(PDF_FILES)) cat output $(OUT)
else
	@$(MERGE) $(sort $(PDF_FILES)) $(OUT)
endif
	@echo "✅ Build complete! Combined file: $(OUT)"

# -----------------------------------------------
# Cleanup utilities
# -----------------------------------------------
clean:
	@echo "🧹 Cleaning auxiliary LaTeX files (keeping logs for debugging)..."
	@rm -f *.aux *.out *.toc *.synctex.gz

cleanall: clean
	@echo "✨ Cleaned temporary files (PDFs + logs retained)."

# -----------------------------------------------
# Full rebuild from scratch
# -----------------------------------------------
rebuild: clean all

.PHONY: all clean cleanall rebuild

