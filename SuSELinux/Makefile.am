#
# Makefile.am for slide-show/slide
#

instdir	= /CD1/suse/setup/slide

# note: txt/*/*.rtf does not work. you get a dir called "txt/*"!
EXTRA_DIST = pic/*.png txt/cs/*.rtf txt/de/*.rtf txt/en/*.rtf	\
	txt/es/*.rtf txt/fr/*.rtf txt/hu/*.rtf txt/it/*.rtf	\
	txt/ja/*.rtf txt/nl/*.rtf txt/sv/*.rtf

install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	cp -a $(srcdir)/txt $(srcdir)/pic $(DESTDIR)/$(instdir)
