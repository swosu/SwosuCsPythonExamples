# Teacher Manual Makefile
PDFLATEX=pdflatex
MAIN=teacher_main

all:
	$(PDFLATEX) $(MAIN).tex
	-@bibtex $(MAIN) || true
	$(PDFLATEX) $(MAIN).tex
	$(PDFLATEX) $(MAIN).tex

clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.lof *.lot *.fls *.fdb_latexmk chapters/*.aux chapters/*.log

view: all
	xdg-open $(MAIN).pdf
