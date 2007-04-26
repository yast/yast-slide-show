#
# Makefile.am for slide-show/slide
#

instdir = /SuSE/SuSE/CD1/suse/setup/slide

# note: txt/*/*.rtf does not work. you get a dir called "txt/*"!

# CAUTION: Czech is "cs", not "cz"! Use the LANG abbrev, not the country!

EXTRA_DIST =					\
	$(fname).xml $(fname).xsl		\
	$(pofiles)				\
	pic/*.png				\
	txt/en/*.rtf				

# 	txt/bg/*.rtf				\
# 	txt/cs/*.rtf				\
# 	txt/da/*.rtf				\
# 	txt/de/*.rtf				\
# 	txt/es/*.rtf				\
# 	txt/et/*.rtf				\
# 	txt/fi/*.rtf				\
# 	txt/fr/*.rtf				\
# 	txt/hu/*.rtf				\
# 	txt/it/*.rtf				\
# 	txt/ja/*.rtf				\
# 	txt/km/*.rtf				\
# 	txt/lt/*.rtf				\
# 	txt/nb/*.rtf				\
# 	txt/nl/*.rtf				\
# 	txt/pl/*.rtf				\
# 	txt/pt/*.rtf				\
# 	txt/pt_BR/*.rtf				\
# 	txt/ru/*.rtf				\
# 	txt/sl/*.rtf				\
# 	txt/sv/*.rtf				\
# 	txt/uk/*.rtf				\
# 	txt/zh_CN/*.rtf				\
# 	txt/zh_TW/*.rtf


fname = slideshow
langs = bg cs da de en es et fi fr hu it ja km lt nb nl pl pt pt_BR ru sl sv uk zh_CN zh_TW
#files = $(foreach l, $(langs), $(fname)_$(l).xml)
#files = $(foreach l, $(langs), $(l).xml)
files = $(addsuffix .xml,$(langs))
out = $(files:.xml=.out)
rtf = $(files:.xml=.rtf)
html = $(files:.xml=.html)
valid = $(files:.xml=.valid)
nochunk = $(files:.xml=.nochunk)
#pofiles = $(files:.xml=.po)
# po/LL.po
pofiles=$(addprefix po/,$(addsuffix .po,$(langs)))
xsl_styles = $(fname).xsl
styles = $(dsssl_styles) $(xsl_styles)

SUFFIXES = .xml .out .rtf .html .valid .po .pot

CLEANFILES = $(out) $(rtf) $(html) $(valid) $(spec) $(files)
newpo:
	echo $(newpo)

arch = @arch@
prod = slprof

XSLTPROC = @XSLTPROC@
# XSLTPROC = xsltproc
XMLLINT = @XMLLINT@
XML2PO = @XML2PO@

MSGMERGE_UPDATE = @MSGMERGE@ --update

outdir:
	rm -fr txt
	mkdir txt

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

rtf: $(rtf)
html: $(html)
all: validate rtf

validate: $(valid)
%.valid: %.xml
	$(XMLLINT) --nonet --valid --noout $< && touch $@

pot: $(fname).pot
$(fname).pot: $(fname).xml
	$(XML2PO) --expand-all-entities -o $(fname).pot $(fname).xml
po: $(pofiles)
$(pofiles): $(fname).pot
	@lang=`echo $@ | sed -e 's,.*/,,' -e 's/\.po$$//'`; \
	echo "$(MSGMERGE_UPDATE) po/$${lang}.po $(fname).pot"; \
	if [ $${lang} = en ]; then \
	  msgen -o po/$${lang}.po $(fname).pot ;\
	else $(MSGMERGE_UPDATE) po/$${lang}.po $(fname).pot ; fi
xml: $(files)
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
