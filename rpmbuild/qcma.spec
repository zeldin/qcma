# 
# qcma spec file
# 

%define _version 0.3.9

%if "%{_version}" == "testing" || "%{_version}" == "master"
%define _verprefix %{_version}
%else
%define _verprefix v%{_version}
%endif

%if 0%{?fedora} || 0%{?centos}
%define _qt5base qt5-qtbase
%define _qt5imageformats qt5-qtimageformats
%define _pkgconfig pkgconfig
%define _qt5toolsdevel qt5-qttools-devel
%define _qt5basedevel qt5-qtbase-devel
%define _knotifications kf5-knotifications
%define _knotifications_devel kf5-knotifications-devel
%define _appindicator libappindicator
%else
%define _qt5base libqt5-qtbase
%define _qt5imageformats libqt5-qtimageformats
%define _pkgconfig pkg-config
%define _qt5toolsdevel libqt5-qttools
%define _qt5basedevel libqt5-qtbase-devel
%define _knotifications libKF5Notifications5
%define _knotifications_devel knotifications-devel
%define _appindicator libappindicator1
%endif

Name:           qcma
Summary:        PSVita Content Manager Assistant
License:        GPL-3.0
Release:        1
Version:        %{_version}
URL:            https://github.com/codestation/qcma
Source:         https://github.com/codestation/qcma/archive/%{_verprefix}/qcma-%{_version}.tar.gz
Group:          Productivity/File utilities
Requires:       libnotify
Requires:       ffmpeg
Requires:       %{_qt5base}
Requires:       %{_qt5imageformats}
Requires:       libvitamtp4 >= 2.5.5
BuildRequires:  gcc-c++ 
BuildRequires:  %{_pkgconfig}
BuildRequires:  libnotify-devel
BuildRequires:  %{_knotifications_devel}
BuildRequires:  libappindicator-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libvitamtp-devel
BuildRequires:  %{_qt5toolsdevel}
BuildRequires:  %{_qt5basedevel}

%description
QCMA is an cross-platform application to provide a Open Source implementation
of the original Content Manager Assistant that comes with the PS Vita. QCMA
is meant to be compatible with Linux, Windows and MAC OS X.

%prep
%setup -n %{name}-%{version}

%build
lrelease-qt5 resources/translations/*.ts
qmake-qt5 PREFIX=/usr qcma.pro CONFIG+="QT5_SUFFIX ENABLE_KNOTIFICATIONS ENABLE_APPINDICATOR ENABLE_KDENOTIFIER"
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/qcma
%{_prefix}/share/applications/qcma/qcma.desktop
%{_prefix}/share/icons/hicolor/64x64/apps/qcma.png

%changelog

%package cli
Summary: Content Manager Assistant for the PS Vita (headless version)
%description cli
Headless version of Qcma
%files cli
%{_bindir}/qcma_cli

%package appindicator
Summary: Content Manager Assistant for the PS Vita (appindicator support)
Requires: %{_appindicator}

%description appindicator
Appindicator plugin for Qcma

%files appindicator
%{_prefix}/lib/qcma/libqcma_appindicator.so
%{_prefix}/share/icons/hicolor/64x64/actions/qcma_on.png
%{_prefix}/share/icons/hicolor/64x64/actions/qcma_off.png

%package kdenotifier
Summary: Content Manager Assistant for the PS Vita (kdenotifier support)
Requires: %{_knotifications}

%description kdenotifier
KDENotifier plugin for Qcma

%files kdenotifier
%{_prefix}/lib/qcma/libqcma_kdenotifier.so
