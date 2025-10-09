# ======================================================
# 📘 RSA Series Makefile — Combine All PDFs
# Author: Jeremy Evert
# ======================================================

LATEX=pdflatex
OUTDIR=output
TEXFILES=$(wildcard ch_04_section_06_RSA*.tex)
PDFFILES=$(patsubst %.tex,$(OUTDIR)/%.pdf,$(TEXFILES))
COMBINED=$(OUTDIR)/RSA_Combined.pdf

# ------------------------------------------------------
# Default target
# ------------------------------------------------------
all: $(OUTDIR) $(COMBINED)
	@echo "✅ All RSA PDFs compiled and combined successfully."

# ------------------------------------------------------
# Rule: build individual PDFs
# ------------------------------------------------------
$(OUTDIR)/%.pdf: %.tex | $(OUTDIR)
	@echo "🧠 Building $< ..."
	@$(LATEX) -interaction=nonstopmode -output-directory=$(OUTDIR) $<
	@$(LATEX) -interaction=nonstopmode -output-directory=$(OUTDIR) $<
	@echo "📄 Generated: $@"

# ------------------------------------------------------
# Rule: combine all PDFs into one
# ------------------------------------------------------
$(COMBINED): $(PDFFILES)
	@echo "🪄 Combining PDFs into one master document..."
	@pdfunite $(PDFFILES) $(COMBINED)
	@echo "🎉 Created: $(COMBINED)"

# ------------------------------------------------------
# Ensure output directory exists
# ------------------------------------------------------
$(OUTDIR):
	@mkdir -p $(OUTDIR)

# ------------------------------------------------------
# Cleaning targets
# ------------------------------------------------------
clean:
	@echo "🧹 Cleaning auxiliary files..."
	@rm -f $(OUTDIR)/*.aux $(OUTDIR)/*.log $(OUTDIR)/*.out $(OUTDIR)/*.toc
	@echo "✅ Auxiliary files removed."

distclean: clean
	@echo "🗑️ Removing generated PDFs..."
	@rm -f $(OUTDIR)/*.pdf
	@echo "✨ Directory reset."

# ------------------------------------------------------
# Rebuild everything from scratch
# ------------------------------------------------------
rebuild: distclean all

.PHONY: all clean distclean rebuild

