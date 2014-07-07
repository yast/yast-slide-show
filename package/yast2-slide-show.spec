#
# spec file for package yast2-slide-show
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-slide-show
Version:        3.1.6
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2


# xml2po uses temporary files that do not like being called twice
# xml2po probably is not thread-safe.
%define jobs 1
BuildRequires:  docbook_4
BuildRequires:  gnome-doc-utils
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
BuildRequires:  yast2-devtools >= 3.1.10
%if 0%{?suse_version} > 1120
# was in gnome-doc-utils before
BuildRequires:  xml2po
%endif
BuildArch:	noarch
Summary:	YaST2 - Slide Show
License:        GPL-2.0
Group:	        Metapackages
Source10:       slideshow-po.tar.gz
Source12:       slideshow-sles-po.tar.gz

%description
The slide show displayed during package installation with YaST.

%package SuSELinux
Summary:	YaST - Slide Show (openSUSE)
Group:		Metapackages

%description SuSELinux
The slide show displayed during package installation with YaST.

%package SLES
Summary:	YaST - Slide Show (SUSE Linux Enterprise Server)
Group:		Metapackages

%description SLES
The slide show displayed during package installation with YaST.

%package SLED
Summary:	YaST - Slide Show (SUSE Linux Enterprise Desktop)
Group:		Metapackages

%description SLED
The slide show displayed during package installation with YaST.

%prep
%setup -n %{name}-%{version}
pushd SuSELinux
tar xf %{S:10}
langs=$(tar tf %{S:10}|sed 's=.*po/==;s=\.po$==;/^$/d'|sort -u|fmt -w1000)
sed -i "s|^langs *=.*$|langs = en $langs|" Makefile.am
popd

pushd SLED
tar xf %{S:12}
langs=$(tar tf %{S:12}|sed 's=.*po/==;s=\.po$==;/^$/d'|sort -u|fmt -w1000)
sed -i "s|^langs *=.*$|langs = en $langs|" Makefile.am
popd

pushd SLES
tar xf %{S:12}
langs=$(tar tf %{S:12}|sed 's=.*po/==;s=\.po$==;/^$/d'|sort -u|fmt -w1000)
sed -i "s|^langs *=.*$|langs = en $langs|" Makefile.am
popd

%build
%yast_build
./tools/check_utf-8
# on OS use the openSUSE logo everywhere; see # 216562
%if %suse_version >= 1020
for f in SuSELinux/txt/*/01*.rtf; do
  sed -i 's/01_welcome.png/02_opensuse.png/' $f
done
%endif

%install
%yast_install

# Get rid of README files etc. auto-created by yast2-devtools
# (but useless for this special package)
/bin/rm -rf %{buildroot}%{_datadir}/doc/packages/yast2-slide-show

# Get rid of test environment during autobuild
/bin/rm -rf %{buildroot}%{_datadir}/YaST2/clients/slide-show.ycp
/bin/rm -rf %{buildroot}%{_datadir}/YaST2/modules/SlideTester.ycp


%files SuSELinux
%defattr(-,root,root)
%dir /SuSE
%dir /SuSE/SuSE
%dir /SuSE/SuSE/CD1
%dir /SuSE/SuSE/CD1/suse
%dir /SuSE/SuSE/CD1/suse/setup
/SuSE/SuSE/CD1/suse/setup/slide/

%files SLES
%defattr(-,root,root)
%dir /SuSE
%dir /SuSE/SuSE-SLES
%dir /SuSE/SuSE-SLES/CD1
%dir /SuSE/SuSE-SLES/CD1/suse
%dir /SuSE/SuSE-SLES/CD1/suse/setup
/SuSE/SuSE-SLES/CD1/suse/setup/slide/

%files SLED
%defattr(-,root,root)
%dir /SuSE
%dir /SuSE/SuSE-SLED
%dir /SuSE/SuSE-SLED/CD1
%dir /SuSE/SuSE-SLED/CD1/suse
%dir /SuSE/SuSE-SLED/CD1/suse/setup
/SuSE/SuSE-SLED/CD1/suse/setup/slide/
