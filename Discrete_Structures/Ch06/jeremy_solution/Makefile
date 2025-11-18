PDF_TARGET = main.pdf
TEX_FILE = main.tex
# List of auxiliary files created by pdflatex
AUX_FILES = *.aux *.log *.toc *.lof *.lot *.out *.synctex.gz *.bbl *.blg

# The default target runs compilation
all: $(PDF_TARGET)

# Rule to compile the PDF. Compiles twice to resolve Table of Contents and references.
$(PDF_TARGET): $(TEX_FILE)
	pdflatex $<
	pdflatex $<

# Rule to clean up auxiliary files and the final PDF
clean:
	@echo "Cleaning auxiliary LaTeX files and PDF..."
	@rm -f $(AUX_FILES) $(PDF_TARGET)

# Rule to open (view) the generated PDF
# Note: The command used here ('open', 'start', 'xdg-open') is dependent on the operating system.
view:
	@echo "Opening $(PDF_TARGET)..."
	@test -f $(PDF_TARGET) && (open $(PDF_TARGET) || start $(PDF_TARGET) || xdg-open $(PDF_TARGET)) || echo "$(PDF_TARGET) not found. Run 'make' first."

.PHONY: all clean view
