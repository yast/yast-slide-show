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
	txt/af/*.rtf                            \
	txt/ar/*.rtf                            \
	txt/bn/*.rtf                            \
	txt/ca/*.rtf                            \
	txt/cs/*.rtf				\
	txt/da/*.rtf				\
	txt/de/*.rtf				\
	txt/es/*.rtf				\
	txt/fi/*.rtf				\
	txt/fr/*.rtf				\
	txt/gu/*.rtf				\
	txt/hi/*.rtf				\
	txt/hu/*.rtf				\
	txt/it/*.rtf				\
	txt/ja/*.rtf				\
	txt/ko/*.rtf				\
	txt/mr/*.rtf				\
	txt/nb/*.rtf				\
	txt/nl/*.rtf				\
	txt/pl/*.rtf				\
	txt/pt_BR/*.rtf				\
	txt/ru/*.rtf                            \
	txt/sv/*.rtf                            \
	txt/ta/*.rtf                            \
	txt/xh/*.rtf                            \
	txt/zh_CN/*.rtf				\
	txt/zh_TW/*.rtf                         \
	txt/zu/*.rtf                            



install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/txt && cp -a $(srcdir)/txt $(DESTDIR)/$(instdir)
	-test -d $(srcdir)/pic && cp -a $(srcdir)/pic $(DESTDIR)/$(instdir)
