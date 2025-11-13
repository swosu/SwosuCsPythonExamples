# Simple Makefile for the example solution project

TEX     = main.tex
PDF     = main.pdf

ASSIGNMENT_SRC := ../assignments/ch05_universe_project.pdf
ASSIGNMENT_DST := files/ch05_universe_project.pdf

all: $(PDF)

$(ASSIGNMENT_DST): $(ASSIGNMENT_SRC)
	@mkdir -p files
	cp $< $@

$(PDF): $(TEX) chapters/*.tex $(ASSIGNMENT_DST)
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(TEX)

view: $(PDF)
	xdg-open $(PDF) >/dev/null 2>&1 &

clean:
	latexmk -C $(TEX)
	rm -f *.run.xml *.synctex.gz

.PHONY: all view clean

