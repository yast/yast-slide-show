#
# Makefile.am for slide-show/slide
#

instdir = /SuSE/SuSE-SLED/CD1/suse/setup/slide

# note: txt/*/*.rtf does not work. you get a dir called "txt/*"!

# CAUTION: Czech is "cs", not "cz"! Use the LANG abbrev, not the country!

EXTRA_DIST =					\
	pic/*.png				\
						\
	txt/en/*.rtf                            \
	txt/cs/*.rtf				\
	txt/da/*.rtf				\
	txt/de/*.rtf				\
	txt/es/*.rtf				\
	txt/fi/*.rtf				\
	txt/fr/*.rtf				\
	txt/hu/*.rtf				\
	txt/it/*.rtf				\
	txt/ja/*.rtf				\
	txt/nb/*.rtf				\
	txt/nl/*.rtf				\
	txt/pl/*.rtf				\
	txt/pt_BR/*.rtf				\
	txt/sl/*.rtf				\
	txt/zh_CN/*.rtf				\
	txt/zh_TW/*.rtf



install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/txt && cp -a $(srcdir)/txt $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/pic && cp -a $(srcdir)/pic $(DESTDIR)/$(instdir)
