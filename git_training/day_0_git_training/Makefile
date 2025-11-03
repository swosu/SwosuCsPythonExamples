# Makefile for Beamer presentation
# Jeremy Evert — Source Code Management slides

TARGET = main
PDF = $(TARGET).pdf

# Default build rule
all: $(PDF)

$(PDF): $(TARGET).tex
	@echo "🧠 Compiling Beamer presentation..."
	latexmk -pdf -interaction=nonstopmode $(TARGET).tex
	@echo "✅ Build complete: $(PDF)"

# Clean auxiliary files
clean:
	@echo "🧹 Cleaning up LaTeX build files..."
	latexmk -c
	rm -f $(PDF)
	@echo "🧼 Clean complete."

# Clean everything except PDF (for when you want to keep your final)
tidy:
	@echo "🧽 Tidying up auxiliary files (keeping PDF)..."
	latexmk -c
	@echo "✨ All tidy!"

# View the final PDF
view:
	@echo "👀 Opening $(PDF)..."
ifeq ($(OS),Windows_NT)
	start $(PDF)
else
	xdg-open $(PDF) || open $(PDF)
endif

# Rebuild from scratch
rebuild: clean all view

