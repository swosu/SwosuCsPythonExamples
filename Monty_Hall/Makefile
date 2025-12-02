# Makefile
DOC := monty_hall_fsm
TEX := $(DOC).tex
DOT := $(DOC).dot
PDF := $(DOC).pdf
SVG := $(DOC).svg

LATEXMK ?= latexmk
DOTBIN  ?= dot

.PHONY: all clean diagrams pdf

all: pdf

diagrams: $(PDF) $(SVG)

$(PDF): $(DOT)
	$(DOTBIN) -Tpdf $< -o $@

$(SVG): $(DOT)
	$(DOTBIN) -Tsvg $< -o $@

pdf: diagrams $(TEX)
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error $(TEX)

clean:
	$(LATEXMK) -C $(TEX) || true
	rm -f $(PDF) $(SVG)

