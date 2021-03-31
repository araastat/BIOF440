OUTDIR = $(shell Rscript -e "cat(fs::path(here::here('docs', fs::path_rel(getwd(), start=here::here()))))")
SLIDES := $(wildcard *.Rmd)
SLIDES_OUT = $(patsubst %.Rmd, $(OUTDIR)/%.html, $(SLIDES))
SLIDES_PDF = $(patsubst %.Rmd, $(OUTDIR)/%.pdf, $(SLIDES))

.PHONY: all
all: $(SLIDES_OUT)
.PHONY: pdf
pdf: $(SLIDES_PDF)

$(OUTDIR)/%.html: %.Rmd 
	Rscript -e "if(!dir.exists('$(OUTDIR)')) dir.create('$(OUTDIR)', recursive=TRUE)"
	Rscript -e "rmarkdown::render('$(*F).Rmd')"
#	rm -rf $(OUTDIR)/$(*F)_files
	mv $(*F).html $(OUTDIR)
#	mv -f $(*F)_files $(OUTDIR)


.PHONY: files
files:
	@echo $(OUTDIR)
	@echo $(SLIDES_OUT)
	@echo $(SLIDES)

.PHONY: clean clean_cache
clean:
	@rm -rf $(SLIDES_OUT)
clean_cache:
	@rm -rf *cache
