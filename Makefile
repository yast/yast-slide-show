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

VERSION = $(shell cat VERSION)
RPMNAME = $(shell cat RPMNAME)
MAINTAINER = $(shell cat MAINTAINER )

SPEC	= package/$(RPMNAME).spec
SPEC_IN	= $(RPMNAME).spec.in

all:
	@echo "Done."
	@echo ""
	@echo "Nothing to really make here. Use 'make package'."
	@echo ""


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


package: clean spec
	rm -f package/$(RPMNAME)-*.tar.bz2 
	tar cIvf $(RPMNAME)-$(VERSION).tar.bz2 --exclude=CVS slide
	mv $(RPMNAME)-$(VERSION).tar.bz2 package

