#
# Makefile.am for slide-show/slide
#

instdir = /SuSE/SuSE/CD1/suse/setup/slide

# note: txt/*/*.rtf does not work. you get a dir called "txt/*"!

# CAUTION: Czech is "cs", not "cz"! Use the LANG abbrev, not the country!

EXTRA_DIST =					\
	pic/*.png				\
						\
	txt/bg/*.rtf				\
	txt/cs/*.rtf				\
	txt/da/*.rtf				\
	txt/de/*.rtf				\
	txt/en/*.rtf				\
	txt/es/*.rtf				\
	txt/fr/*.rtf				\
	txt/hu/*.rtf				\
	txt/it/*.rtf				\
	txt/ja/*.rtf				\
	txt/nl/*.rtf				\
	txt/no/*.rtf				\
	txt/sl/*.rtf				\
	txt/sv/*.rtf



install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	cp -a $(srcdir)/txt $(srcdir)/pic $(DESTDIR)/$(instdir)
