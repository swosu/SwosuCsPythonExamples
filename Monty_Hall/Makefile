# Monty_Hall/Makefile

DOC := monty_hall_project
TEX := $(DOC).tex

LATEXMK ?= latexmk
DOTBIN  ?= dot

# Build every DOT diagram in diagrams/
DOTS      := $(wildcard diagrams/*.dot)
DIAG_PDFS := $(DOTS:.dot=.pdf)
DIAG_SVGS := $(DOTS:.dot=.svg)

.PHONY: all pdf diagrams view clean

all: pdf

# --- Diagrams ---
diagrams: $(DIAG_PDFS) $(DIAG_SVGS)

diagrams/%.pdf: diagrams/%.dot
	$(DOTBIN) -Tpdf $< -o $@

diagrams/%.svg: diagrams/%.dot
	$(DOTBIN) -Tsvg $< -o $@

# --- LaTeX ---
pdf: diagrams
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error $(TEX)

view: pdf
	xdg-open $(DOC).pdf >/dev/null 2>&1 & disown

clean:
	$(LATEXMK) -C $(TEX) || true
	rm -f $(DIAG_PDFS) $(DIAG_SVGS)

