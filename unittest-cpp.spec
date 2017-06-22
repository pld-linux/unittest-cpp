#
# Conditional build:
%bcond_without	tests	# check target
#
Summary:	Lightweight unit testing framework for C++
Summary(pl.UTF-8):	Lekki szkielet testów jednostkowych dla C++
Name:		unittest-cpp
Version:	2.0.0
Release:	1
Group:		Libraries
License:	MIT
#Source0Download: https://github.com/unittest-cpp/unittest-cpp/releases
Source0:	https://github.com/unittest-cpp/unittest-cpp/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	48f4fa972c5b1462098f8a4352b5d0cc
Patch0:		%{name}-sh.patch
URL:		https://github.com/unittest-cpp/unittest-cpp
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UnitTest++ is a lightweight unit testing framework for C++.
Simplicity, portability, speed, and small footprint are all very
important aspects of UnitTest++.

%package devel
Summary:	Development files for UnitTest++
Summary(pl.UTF-8):	Pliki programistyczne biblioteki UnitTest++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files necessary for developing
test programs.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne potrzebne do tworzenia
programów testowych.

%package static
Summary:	Static UnitTest++ library
Summary(pl.UTF-8):	Statyczna biblioteka UnitTest++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static library necessary for statically linking
test programs.

%description static -l pl.UTF-8
Ten pakiet zawiera bibliotekę statyczną potrzebną do statycznego
linkowania programów testowych.

%prep
%setup -q
%patch0 -p1

# git data not available, hardcode released package version
%{__sed} -i -e 's/m4_esyscmd_s.*git describe --tags.*/[%{version}],/' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libUnitTest++.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libUnitTest++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libUnitTest++.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libUnitTest++.so
%{_includedir}/UnitTest++
%{_pkgconfigdir}/UnitTest++.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libUnitTest++.a
