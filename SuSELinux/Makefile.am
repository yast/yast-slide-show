#
# Makefile.am for slide-show/slide
#

instdir = /SuSE/SuSE/CD1/suse/setup/slide

# note: txt/*/*.rtf does not work. you get a dir called "txt/*"!

EXTRA_DIST =					\
	pic/*.png				\
						\
	txt/en/*.rtf				\
	txt/de/*.rtf				\
	txt/cs/*.rtf				\
	txt/es/*.rtf				\
	txt/fr/*.rtf				\
	txt/it/*.rtf				\
	txt/nl/*.rtf				\
	txt/bg/*.rtf				\
	txt/sk/*.rtf				\
	txt/hu/*.rtf

install-data-local:
	mkdir -p $(DESTDIR)/$(instdir)
	cp -a $(srcdir)/txt $(srcdir)/pic $(DESTDIR)/$(instdir)
