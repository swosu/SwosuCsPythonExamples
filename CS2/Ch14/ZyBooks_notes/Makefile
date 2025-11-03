# Makefile for CS2 Recursion Workbook
# Jeremy Evert, SWOSU

PDFLATEX=pdflatex
LATEXMK=latexmk
TARGET=main

all:
	@echo "🧠 Compiling LaTeX workbook..."
	$(LATEXMK) -pdf -interaction=nonstopmode $(TARGET).tex

clean:
	@echo "🧹 Cleaning up LaTeX build files..."
	$(LATEXMK) -c
	rm -f $(TARGET).pdf

view: all
	@echo "📖 Opening PDF..."
	xdg-open $(TARGET).pdf >/dev/null 2>&1 || open $(TARGET).pdf


