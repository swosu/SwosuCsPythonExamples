# Makefile for Ch04 LaTeX workflow

# Detect all .tex files
TEX_FILES := $(wildcard *.tex)
PDF_FILES := $(TEX_FILES:.tex=.pdf)

# Student and Teacher sets (pattern match on filename)
STUDENT_PDFS := $(filter-out %teacher.pdf, $(PDF_FILES))
TEACHER_PDFS := $(filter %teacher.pdf, $(PDF_FILES))

# Default target
all: clean build combine

# Compile all PDFs
build: $(PDF_FILES)

%.pdf: %.tex
	pdflatex -interaction=nonstopmode $<

# Remove junk files
clean:
	rm -f *.aux *.log *.out *.toc

# Combine student and teacher PDFs separately
combine: student_worksheets.pdf teacher_solutions.pdf

student_worksheets.pdf: $(STUDENT_PDFS)
	pdfunite $^ $@

teacher_solutions.pdf: $(TEACHER_PDFS)
	pdfunite $^ $@

# Full cleanup (removes compiled PDFs too)
distclean: clean
	rm -f *.pdf

