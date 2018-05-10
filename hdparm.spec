#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hdparm
Version  : 9.56
Release  : 12
URL      : https://sourceforge.net/projects/hdparm/files/hdparm/hdparm-9.56.tar.gz
Source0  : https://sourceforge.net/projects/hdparm/files/hdparm/hdparm-9.56.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: hdparm-bin
Requires: hdparm-doc

%description
These files were contributed by various users.
=====================================================================

%package bin
Summary: bin components for the hdparm package.
Group: Binaries

%description bin
bin components for the hdparm package.


%package doc
Summary: doc components for the hdparm package.
Group: Documentation

%description doc
doc components for the hdparm package.


%prep
%setup -q -n hdparm-9.56

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522106925
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1522106925
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hdparm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*
