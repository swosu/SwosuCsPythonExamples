DOC := monty_hall_fsm
TEX := $(DOC).tex
DOT := $(DOC).dot

DIAG_PDF := $(DOC)_diagram.pdf
DIAG_SVG := $(DOC)_diagram.svg

LATEXMK ?= latexmk
DOTBIN  ?= dot

.PHONY: all clean diagrams pdf view

all: pdf

diagrams: $(DIAG_PDF) $(DIAG_SVG)

$(DIAG_PDF): $(DOT)
	$(DOTBIN) -Tpdf $< -o $@

$(DIAG_SVG): $(DOT)
	$(DOTBIN) -Tsvg $< -o $@

pdf: diagrams $(TEX)
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error $(TEX)

view: pdf
	xdg-open $(DOC).pdf >/dev/null 2>&1 & disown

clean:
	$(LATEXMK) -C $(TEX) || true
	rm -f $(DIAG_PDF) $(DIAG_SVG)

