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
	txt/el/*.rtf				\
	txt/en/*.rtf				\
	txt/es/*.rtf				\
	txt/fr/*.rtf				\
	txt/hu/*.rtf				\
	txt/it/*.rtf				\
	txt/ja/*.rtf				\
	txt/nl/*.rtf				\
	txt/no/*.rtf				\
	txt/sk/*.rtf				\
	txt/sl/*.rtf				\
	txt/uk/*.rtf				\
	txt/zh_CN/*.rtf				\
	txt/zh_TW/*.rtf



install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/txt && cp -a $(srcdir)/txt $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/pic && cp -a $(srcdir)/pic $(DESTDIR)/$(instdir)
