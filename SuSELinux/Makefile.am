#
# Makefile.am for slide-show/SuSELinux
#

instdir = /SuSE/SuSE/CD1/suse/setup/slide

fname = slideshow

# list of languages available in SVN
# CAUTION: Czech is "cs", not "cz"! Use the LANG abbrev, not the country!
langs = en en_GB cs da de el fi fr hu it km lt nb nl pa pl pt ru sk uk zh_TW

# list of languages ready for distribution _and_ installation
dist_langs = $(langs)
# take the files from txt/LL/*.rtf
# txt/*/*.rtf does not work. you get a dir called "txt/*"!
dist_lang_files = $(addprefix txt/,$(addsuffix /*.rtf,$(dist_langs)))

EXTRA_DIST =					\
	$(fname).xml $(xsl_styles)		\
	$(pofiles)				\
	pic/*.png				\
	$(dist_lang_files)

xml = $(addsuffix .xml,$(langs))
rtf = $(xml:.xml=.rtf)
valid = $(xml:.xml=.valid)
# nochunk = $(xml:.xml=.nochunk)
#pofiles = $(xml:.xml=.po)
# po/LL.po
pofiles=$(addprefix po/,$(addsuffix .po,$(langs)))
xsl_styles = $(fname).xsl

SUFFIXES = .xml .rtf .valid .po .pot

CLEANFILES = $(rtf) $(valid) $(xml) $(fname).pot

XSLTPROC = @XSLTPROC@
XMLLINT = @XMLLINT@
XML2PO = @XML2PO@

MSGMERGE_UPDATE = @MSGMERGE@ --update

all: validate rtf

outdir:
	rm -fr txt
	mkdir txt

rtf: $(rtf)
%.rtf: %.xml outdir
	ll=`echo $< | sed "s/\.xml$$//"`; \
	  mkdir txt/$$ll ; \
	  $(XSLTPROC) --nonet --stringparam out.dir "txt/$$ll" \
	    $(fname).xsl $< 1>/dev/null; \
	  pushd txt/$$ll ; \
          for f in *.rtf ; do \
	    sed -i 's/\/>/>/;s/%imagedir%/\&imagedir;/' $$f; \
	  done ; \
	  popd

validate: $(valid)
%.valid: %.xml
	$(XMLLINT) --nonet --valid --noout $< && touch $@

pot: $(fname).pot
$(fname).pot: $(fname).xml
	$(XML2PO) --expand-all-entities -o $(fname).pot $(fname).xml

# re-merge po translation files
po: $(pofiles)
$(pofiles): $(fname).pot
	@lang=`echo $@ | sed -e 's,.*/,,' -e 's/\.po$$//'`; \
	echo "$(MSGMERGE_UPDATE) po/$${lang}.po $(fname).pot"; \
	if [ $${lang} = en ]; then \
	  msgen -o po/$${lang}.po $(fname).pot ;\
	else $(MSGMERGE_UPDATE) po/$${lang}.po $(fname).pot ; fi

xml: $(xml)
%.xml: po/%.po
	@lang=`echo $@ | sed -e 's,.*/,,' -e 's,$(fname)_/,,' -e 's/\.xml$$//'`; \
	echo "$(XML2PO) -p po/$${lang}.po -o $${lang}.xml $(fname).pot"; \
	$(XML2PO) -p po/$${lang}.po -o $${lang}.xml $(fname).xml

# rndir=$(DESTDIR)$(datadir)/doc/$(PACKAGE_NAME)
install-data-local:
#	$(mkinstalldirs) $(rndir)
#	for file in $(html); do \
#	  $(INSTALL_DATA) $$file $(rndir) ; \
#	done
	mkdir -p $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/txt && cp -a $(srcdir)/txt $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/pic && cp -a $(srcdir)/pic $(DESTDIR)/$(instdir)
