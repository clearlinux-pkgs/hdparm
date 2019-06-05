#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hdparm
Version  : 9.58
Release  : 15
URL      : https://sourceforge.net/projects/hdparm/files/hdparm/hdparm-9.58.tar.gz
Source0  : https://sourceforge.net/projects/hdparm/files/hdparm/hdparm-9.58.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: hdparm-bin = %{version}-%{release}
Requires: hdparm-license = %{version}-%{release}
Requires: hdparm-man = %{version}-%{release}

%description
These files were contributed by various users.
=====================================================================

%package bin
Summary: bin components for the hdparm package.
Group: Binaries
Requires: hdparm-license = %{version}-%{release}
Requires: hdparm-man = %{version}-%{release}

%description bin
bin components for the hdparm package.


%package license
Summary: license components for the hdparm package.
Group: Default

%description license
license components for the hdparm package.


%package man
Summary: man components for the hdparm package.
Group: Default

%description man
man components for the hdparm package.


%prep
%setup -q -n hdparm-9.58

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540564821
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1540564821
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hdparm
cp LICENSE.TXT %{buildroot}/usr/share/package-licenses/hdparm/LICENSE.TXT
cp debian/copyright %{buildroot}/usr/share/package-licenses/hdparm/debian_copyright
cp wiper/GPLv2.txt %{buildroot}/usr/share/package-licenses/hdparm/wiper_GPLv2.txt
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hdparm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hdparm/LICENSE.TXT
/usr/share/package-licenses/hdparm/debian_copyright
/usr/share/package-licenses/hdparm/wiper_GPLv2.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/hdparm.8
