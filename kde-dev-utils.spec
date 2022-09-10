#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kde-dev-utils
Version  : 22.08.1
Release  : 44
URL      : https://download.kde.org/stable/release-service/22.08.1/src/kde-dev-utils-22.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.1/src/kde-dev-utils-22.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.08.1/src/kde-dev-utils-22.08.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0 LGPL-3.0
Requires: kde-dev-utils-bin = %{version}-%{release}
Requires: kde-dev-utils-data = %{version}-%{release}
Requires: kde-dev-utils-lib = %{version}-%{release}
Requires: kde-dev-utils-license = %{version}-%{release}
Requires: kde-dev-utils-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-dev

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
%setup -q -n kde-dev-utils-22.08.1
cd %{_builddir}/kde-dev-utils-22.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662783361
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1662783361
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-dev-utils
cp %{_builddir}/kde-dev-utils-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kde-dev-utils/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kde-dev-utils-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kde-dev-utils/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kde-dev-utils-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kde-dev-utils/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kde-dev-utils-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kde-dev-utils/e458941548e0864907e654fa2e192844ae90fc32
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
/usr/share/metainfo/org.kde.kuiviewer.metainfo.xml
/usr/share/metainfo/org.kde.kuiviewerpart.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/parts/kuiviewerpart.so
/usr/lib64/qt5/plugins/quithumbnail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-dev-utils/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kde-dev-utils/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kde-dev-utils/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kuiviewer.lang -f kpartloader.lang
%defattr(-,root,root,-)

