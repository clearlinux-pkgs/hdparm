#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hdparm
Version  : 9.62
Release  : 19
URL      : https://sourceforge.net/projects/hdparm/files/hdparm/hdparm-9.62.tar.gz
Source0  : https://sourceforge.net/projects/hdparm/files/hdparm/hdparm-9.62.tar.gz
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
%setup -q -n hdparm-9.62
cd %{_builddir}/hdparm-9.62

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620667372
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1620667372
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hdparm
cp %{_builddir}/hdparm-9.62/LICENSE.TXT %{buildroot}/usr/share/package-licenses/hdparm/88e79deadef14cb3a3ca419bb731f1deb5ffa7c3
cp %{_builddir}/hdparm-9.62/debian/copyright %{buildroot}/usr/share/package-licenses/hdparm/521ecd1edcba0923d0ffbf7ae9af6726d97afe78
cp %{_builddir}/hdparm-9.62/wiper/GPLv2.txt %{buildroot}/usr/share/package-licenses/hdparm/ef1bcf369e4124b5f2558fefee17972f41b76cab
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hdparm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hdparm/521ecd1edcba0923d0ffbf7ae9af6726d97afe78
/usr/share/package-licenses/hdparm/88e79deadef14cb3a3ca419bb731f1deb5ffa7c3
/usr/share/package-licenses/hdparm/ef1bcf369e4124b5f2558fefee17972f41b76cab

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/hdparm.8
