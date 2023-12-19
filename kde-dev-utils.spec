#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kde-dev-utils
Version  : 23.08.4
Release  : 62
URL      : https://download.kde.org/stable/release-service/23.08.4/src/kde-dev-utils-23.08.4.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.4/src/kde-dev-utils-23.08.4.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.4/src/kde-dev-utils-23.08.4.tar.xz.sig
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
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kde-dev-utils-23.08.4
cd %{_builddir}/kde-dev-utils-23.08.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702978573
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702978573
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-dev-utils
cp %{_builddir}/kde-dev-utils-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kde-dev-utils/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kde-dev-utils-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kde-dev-utils/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kde-dev-utils-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kde-dev-utils/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kde-dev-utils-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kde-dev-utils/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kuiviewer
%find_lang kpartloader
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kpartloader
/V3/usr/bin/kuiviewer
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
/V3/usr/lib64/qt5/plugins/kf5/parts/kuiviewerpart.so
/V3/usr/lib64/qt5/plugins/quithumbnail.so
/usr/lib64/qt5/plugins/kf5/parts/kuiviewerpart.so
/usr/lib64/qt5/plugins/quithumbnail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-dev-utils/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kde-dev-utils/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kde-dev-utils/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kuiviewer.lang -f kpartloader.lang
%defattr(-,root,root,-)

