DOC := monty_hall_project
TEX := $(DOC).tex

DOT := diagrams/monty_hall_fsm.dot
DIAG_PDF := diagrams/monty_hall_fsm_diagram.pdf
DIAG_SVG := diagrams/monty_hall_fsm_diagram.svg

LATEXMK ?= latexmk
DOTBIN  ?= dot

.PHONY: all pdf diagrams clean view

all: pdf

diagrams: $(DIAG_PDF) $(DIAG_SVG)

$(DIAG_PDF): $(DOT)
	$(DOTBIN) -Tpdf $< -o $@

$(DIAG_SVG): $(DOT)
	$(DOTBIN) -Tsvg $< -o $@

pdf: diagrams
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error $(TEX)

view: pdf
	xdg-open $(DOC).pdf >/dev/null 2>&1 & disown

clean:
	$(LATEXMK) -C $(TEX) || true
	rm -f $(DIAG_PDF) $(DIAG_SVG)

