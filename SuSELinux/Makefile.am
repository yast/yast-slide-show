#
# Makefile.am for slide-show/slide
#

instdir = /SuSE/SuSE/CD1/suse/setup/slide

# note: txt/*/*.rtf does not work. you get a dir called "txt/*"!

# CAUTION: Czech is "cs", not "cz"! Use the LANG abbrev, not the country!

EXTRA_DIST =					\
	pic/*.png				\
						\
	txt/cs/*.rtf				\
	txt/de/*.rtf				\
	txt/dk/*.rtf				\
	txt/en/*.rtf				\
	txt/es/*.rtf				\
	txt/hu/*.rtf				\
	txt/ja/*.rtf				\
	txt/nl/*.rtf				\
	txt/no/*.rtf				\
	txt/sl/*.rtf



install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	cp -a $(srcdir)/txt $(srcdir)/pic $(DESTDIR)/$(instdir)
