#
# Makefile.am for slide-show/slide
#

instdir	= /CD1/suse/setup/slide-SLES

# note: txt/*/*.rtf does not work. you get a dir called "txt/*"!
EXTRA_DIST = pic/*.png \
	   txt/cs/*.rtf \
	   txt/de/*.rtf \
	   txt/en/*.rtf

install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	cp -a $(srcdir)/txt $(srcdir)/pic $(DESTDIR)/$(instdir)
