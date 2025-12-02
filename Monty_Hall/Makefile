DOTS := $(wildcard diagrams/*.dot)
DIAG_PDFS := $(DOTS:.dot=.pdf)
DIAG_SVGS := $(DOTS:.dot=.svg)

diagrams: $(DIAG_PDFS) $(DIAG_SVGS)

diagrams/%.pdf: diagrams/%.dot
	$(DOTBIN) -Tpdf $< -o $@

diagrams/%.svg: diagrams/%.dot
	$(DOTBIN) -Tsvg $< -o $@

