#
# Makefile.am for slide-show/slide
#

instdir = /SuSE/SuSE/CD1/suse/setup/slide

# note: txt/*/*.rtf does not work. you get a dir called "txt/*"!

# CAUTION: Czech is "cs", not "cz"! Use the LANG abbrev, not the country!

EXTRA_DIST =					\
	pic/*.png				\
						\
	txt/en/*.rtf				\
	txt/bg/*.rtf				\
	txt/cs/*.rtf				\
	txt/de/*.rtf				\
	txt/el/*.rtf				\
	txt/es/*.rtf				\
	txt/it/*.rtf				\
	txt/ja/*.rtf				\
	txt/nl/*.rtf				\
	txt/no/*.rtf				\
	txt/pl/*.rtf				\
	txt/sk/*.rtf				\
	txt/sl/*.rtf



install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/txt && cp -a $(srcdir)/txt $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/pic && cp -a $(srcdir)/pic $(DESTDIR)/$(instdir)
