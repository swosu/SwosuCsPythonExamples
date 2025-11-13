# Simple latexmk Makefile for a single main .tex
MAIN=Ch_6_HW_Example

.PHONY: all clean view

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex $(wildcard chapters/*.tex)
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

view: $(MAIN).pdf
	xdg-open $(MAIN).pdf >/dev/null 2>&1 || open $(MAIN).pdf || true

clean:
	latexmk -C $(MAIN).tex
	rm -f *.run.xml *.synctex.gz

