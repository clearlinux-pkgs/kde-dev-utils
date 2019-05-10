#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kde-dev-utils
Version  : 19.04.1
Release  : 7
URL      : https://download.kde.org/stable/applications/19.04.1/src/kde-dev-utils-19.04.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.1/src/kde-dev-utils-19.04.1.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.1/src/kde-dev-utils-19.04.1.tar.xz.sig
Summary  : Small utilities for developers using KDE/Qt libs/frameworks
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: kde-dev-utils-bin = %{version}-%{release}
Requires: kde-dev-utils-data = %{version}-%{release}
Requires: kde-dev-utils-lib = %{version}-%{release}
Requires: kde-dev-utils-license = %{version}-%{release}
Requires: kde-dev-utils-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qttools-staticdev

%description
No detailed description available

%package bin
Summary: bin components for the kde-dev-utils package.
Group: Binaries
Requires: kde-dev-utils-data = %{version}-%{release}
Requires: kde-dev-utils-license = %{version}-%{release}

%description bin
bin components for the kde-dev-utils package.


%package data
Summary: data components for the kde-dev-utils package.
Group: Data

%description data
data components for the kde-dev-utils package.


%package lib
Summary: lib components for the kde-dev-utils package.
Group: Libraries
Requires: kde-dev-utils-data = %{version}-%{release}
Requires: kde-dev-utils-license = %{version}-%{release}

%description lib
lib components for the kde-dev-utils package.


%package license
Summary: license components for the kde-dev-utils package.
Group: Default

%description license
license components for the kde-dev-utils package.


%package locales
Summary: locales components for the kde-dev-utils package.
Group: Default

%description locales
locales components for the kde-dev-utils package.


%prep
%setup -q -n kde-dev-utils-19.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557520457
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557520457
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-dev-utils
cp COPYING %{buildroot}/usr/share/package-licenses/kde-dev-utils/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kde-dev-utils/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kuiviewer
%find_lang kpartloader

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kpartloader
/usr/bin/kuiviewer

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kuiviewer.desktop
/usr/share/icons/hicolor/128x128/apps/kuiviewer.png
/usr/share/icons/hicolor/16x16/apps/kuiviewer.png
/usr/share/icons/hicolor/32x32/apps/kuiviewer.png
/usr/share/icons/hicolor/48x48/apps/kuiviewer.png
/usr/share/icons/hicolor/64x64/apps/kuiviewer.png
/usr/share/icons/hicolor/scalable/apps/kuiviewer.svg
/usr/share/kservices5/designerthumbnail.desktop
/usr/share/kservices5/kuiviewer_part.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/parts/kuiviewerpart.so
/usr/lib64/qt5/plugins/quithumbnail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-dev-utils/COPYING
/usr/share/package-licenses/kde-dev-utils/COPYING.LIB

%files locales -f kuiviewer.lang -f kpartloader.lang
%defattr(-,root,root,-)

