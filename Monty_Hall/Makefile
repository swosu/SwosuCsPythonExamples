# Monty_Hall/Makefile

DOC := monty_hall_project
TEX := $(DOC).tex

LATEXMK ?= latexmk
DOTBIN  ?= dot
RM      ?= rm -f

# Build every DOT diagram in diagrams/
DOTS      := $(wildcard diagrams/*.dot)
DIAG_PDFS := $(DOTS:.dot=.pdf)
DIAG_SVGS := $(DOTS:.dot=.svg)

# Handy: all chapter inputs
CHAPTERS := $(wildcard chapters/*.tex)

.PHONY: all diagrams view clean clean-tex clean-diagrams

# Default target
all: $(DOC).pdf

# --- Main PDF build ---
# The order-only prereq (| diagrams) says:
# “ensure diagrams exist first, but changes in the *directory timestamp* won’t rebuild the PDF.”
$(DOC).pdf: $(TEX) $(CHAPTERS) references.bib | diagrams
	@set -e; \
	echo "[make] building $(DOC).pdf"; \
	if $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error $(TEX); then \
	  : ; \
	else \
	  echo "[make] bibtex got spicy; rebuilding without running bibtex (PDF will still update)"; \
	  $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error -bibtex- $(TEX); \
	fi


# --- Diagrams ---
diagrams: $(DIAG_PDFS) $(DIAG_SVGS)

diagrams/%.pdf: diagrams/%.dot
	$(DOTBIN) -Tpdf $< -o $@

diagrams/%.svg: diagrams/%.dot
	$(DOTBIN) -Tsvg $< -o $@

# --- Convenience ---
view: $(DOC).pdf
	xdg-open $(DOC).pdf >/dev/null 2>&1 & disown

# --- Cleaning ---
clean: clean-tex clean-diagrams

clean-tex:
	$(LATEXMK) -C $(TEX) || true

clean-diagrams:
	$(RM) $(DIAG_PDFS) $(DIAG_SVGS)

