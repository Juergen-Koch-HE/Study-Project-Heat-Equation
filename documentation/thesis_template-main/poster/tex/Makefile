PAPER = poster

SED_IS_GNU=$(shell sed --version 2>&1 | grep "GNU")
ifeq ($(SED_IS_GNU),)
SED=sed -i "" -E
else
SED=sed -i -r
endif


poster: 
	"pdflatex" -draftmode $(PAPER).tex || true
	"bibtex" $(PAPER).aux
	#"makeglossaries" $(PAPER)
	"pdflatex" -draftmode $(PAPER).tex
	"pdflatex" -synctex=1 -interaction=nonstopmode $(PAPER).tex

cleanposter:
	rm -f $(PAPER).pdf $(PAPER).aux $(PAPER).bbl $(PAPER).blg $(PAPER).log $(PAPER).synctex.gz $(PAPER).out $(PAPER).toc $(PAPER).lpr $(PAPER).lot $(PAPER).lof $(PAPER).dvi $(PAPER).snm $(PAPER)-blx.bib $(PAPER).nav $(PAPER).run.xml



# make each sentence start on a new line (to reduce line-based conflicts)
# this doesn't touch lines which contain a percent sign, you'll have to fix those manually.
texnewlines: *.tex
	@$(SED) '/(\%|\\)/! s/\.[[:space:]]+([A-ZÄÖÜ])/.\n\
\1/g' $^

# unclutter:
# - remove trailing white space
# - use non-breaking space (~) in front of citations and references
texclean: *.tex
	@$(SED) 's/[[:space:]]+$$//g' $^
	@$(SED) '/%/! s/[[:space:]]+\\(cite|ref)\{/~\\\1{/g' $^
