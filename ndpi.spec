%global _hardened_build 1

Summary:    Open source deep packet inspection
Name:       nDPI
Version:    1.8
Release:    1%{?dist}
License:    GPLv2
Group:      System Environment/Daemons
URL:        https://github.com/ntop/nDPI

Source0:    https://github.com/ntop/nDPI/archive/%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: autogen
#BuildRequires:	gettext-devel
BuildRequires: gcc
BuildRequires: git
BuildRequires: libpcap-devel
BuildRequires: libtool
BuildRequires: make

Requires:      libpcap

%description
nDPI is a ntop-maintained superset of the popular OpenDPI
library. Released under the GPL license, its goal is to extend the
original library by adding new protocols that are otherwise available
only on the paid version of OpenDPI. In addition to Unix platforms,
we also support Windows, in order to provide you a cross-platform DPI
experience. Furthermore, we have modified nDPI do be more suitable for
traffic monitoring applications, by disabling specific features that
slow down the DPI engine while being them un-necessary for network
traffic monitoring.

nDPI is used by both ntop and nProbe for adding application-layer
detection of protocols, regardless of the port being used. This means
that it is possible to both detect known protocols on non-standard
ports (e.g. detect http non ports other than 80), and also the opposite
(e.g. detect Skype traffic on port 80). This is because nowadays the
concept of port=application no longer holds.

%package	devel
Summary:	Header files and libraries for developing applications for nDPI
Group:		Development/Libraries
Requires:	nDPI = %{version}-%{release}

%description	devel
These are the header files and libraries for developing applications for nDPI.

%prep
%autosetup

%build
./autogen.sh
./configure --prefix %{_prefix} --libdir=%{_libdir} --with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*
%{_libdir}/pkgconfig/libndpi.pc
%{_bindir}/ndpiReader

%files devel
%defattr(-,root,root,-)
%doc COPYING README.md README.nDPI README.protocols
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Fri Oct 14 2016 John Siegrist <john@complects.com> - 1.8-1
- Initial packaging for the CloudRouter distribution
