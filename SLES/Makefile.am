#
# Makefile.am for slide-show/slide
#

instdir	= /SuSE/SuSE-SLES/CD1/suse/setup/slide

# note: txt/*/*.rtf does not work. you get a dir called "txt/*"!
EXTRA_DIST = pic/*.png \
	   txt/cs/*.rtf \
	   txt/de/*.rtf \
	   txt/en/*.rtf

install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	test -d $(srcdir)/txt && cp -a $(srcdir)/txt $(DESTDIR)/$(instdir)
	test -d $(srcdir)/pic && cp -a $(srcdir)/pic $(DESTDIR)/$(instdir)
