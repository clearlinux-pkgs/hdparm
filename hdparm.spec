#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hdparm
Version  : 9.48
Release  : 2
URL      : http://downloads.sourceforge.net/project/hdparm/hdparm/hdparm-9.48.tar.gz
Source0  : http://downloads.sourceforge.net/project/hdparm/hdparm/hdparm-9.48.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
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
%setup -q -n hdparm-9.48

%build
make V=1  %{?_smp_mflags}

%install
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
