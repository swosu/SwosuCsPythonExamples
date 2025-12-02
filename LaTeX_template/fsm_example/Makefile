DIAGRAMS = fsm

all: $(DIAGRAMS:%=%.pdf)

%.pdf: %.dot
	dot -Tpdf $< -o $@

clean:
	rm -f *.pdf

