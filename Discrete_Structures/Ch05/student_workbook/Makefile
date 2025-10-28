all:
	pdflatex main.tex
	bibtex main.aux || true
	pdflatex main.tex
	pdflatex main.tex

clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg

