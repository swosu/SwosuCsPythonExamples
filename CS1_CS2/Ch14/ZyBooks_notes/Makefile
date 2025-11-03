# Simple Makefile for Recursion Workbook

TEX = main.tex
PDF = main.pdf

all: $(PDF)

$(PDF): $(TEX)
	@echo "🧠 Compiling LaTeX..."
	latexmk -pdf -interaction=nonstopmode $(TEX)

clean:
	@echo "🧹 Cleaning up LaTeX build files..."
	latexmk -c

view: $(PDF)
	@echo "👀 Opening PDF..."
	xdg-open $(PDF) &

.PHONY: all clean view

