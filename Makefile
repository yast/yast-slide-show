#
# Makefile for the YaST2 slide show
#
# Author: Stefan Hundhammer <sh@suse.de>
#
# $Id$
#
# Unlike most YaST2 Makefiles, this file is NOT automatically generated,
# so don't simply delete it.
#
# This Makefile will automatically be copied into the dist subdir upon
# "make dist".
#

VERSION 	= $(shell cat VERSION)
RPMNAME 	= $(shell cat RPMNAME)
MAINTAINER	= $(shell cat MAINTAINER )
distdir 	= $(RPMNAME)-$(VERSION)
instdir		= /CD1/suse/setup

# Add all files outside the "slide" subdir that are to go into the tarball 
# to this list
EXTRA_DIST = 					\
	RPMNAME 				\
	VERSION 				\
	MAINTAINER 				\
	Makefile				\
	COPYING					\
	COPYRIGHT.english			\
	COPYRIGHT.french			\
	COPYRIGHT.german


SPEC	= package/$(RPMNAME).spec
SPEC_IN	= $(RPMNAME).spec.in


all:
	@echo "Done."
	@echo ""
	@echo "Nothing to really make here. Use 'make package'."
	@echo ""


install:
	mkdir -p $(instdir)
	cp -a slide $(instdir)

debug:
	@echo "Name: $(RPMNAME)-$(VERSION)"
	@echo "Spec file:    $(SPEC)"
	@echo "Spec.in file: $(SPEC_IN)"


$(SPEC): $(SPEC_IN) VERSION RPMNAME MAINTAINER
	sed <$(SPEC_IN) >$(SPEC)	\
	-e "s/@VERSION@/$(VERSION)/"	\
	-e "s/@RPMNAME@/$(RPMNAME)/"	\
	-e "s/@MAINTAINER@/$(MAINTAINER)/"


spec:	$(SPEC)


clean:
	find . \( -name "*.bak" -o -name "*.auto" -o -name "*~" \) -print -exec rm {} \;


clean-dist:
	-rm -rf $(distdir)


dist:	clean-dist
	mkdir $(distdir)
	cp -a slide $(distdir)
	find $(distdir) -name CVS -print | xargs rm -rf
	cp $(EXTRA_DIST) $(distdir)


package: clean spec dist
	rm -f package/$(RPMNAME)-*.tar.bz2
	tar cIf $(RPMNAME)-$(VERSION).tar.bz2 $(distdir)
	rm -rf $(distdir)
	mv $(RPMNAME)-$(VERSION).tar.bz2 package


stable: package
	y2tool checkin-stable
