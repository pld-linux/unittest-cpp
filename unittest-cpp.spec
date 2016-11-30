%bcond_without	tests
Summary:	Lightweight unit testing framework for C++
Name:		unittest-cpp
Version:	1.6.1
Release:	1
Group:		Libraries
License:	MIT
URL:		https://github.com/unittest-cpp/unittest-cpp
Source0:	https://github.com/unittest-cpp/unittest-cpp/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b4849a686b78ba198a51a49966b8ddba
BuildRequires:	autoconf
BuildRequires:	libtool

%description
%{name} is a lightweight unit testing framework for C++. Simplicity,
portability, speed, and small footprint are all very important aspects
of %{name}.

%package devel
Summary:	Object files for development using %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the object files necessary for
developing test programs.

%package static
Summary:	Static library for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
The %{name}-static package contains the object files necessary for
statically linking test programs.

%prep
%setup -q

%build
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libUnitTest++.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libUnitTest++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libUnitTest++.so.1

%files devel
%defattr(644,root,root,755)
%{_includedir}/UnitTest++
%attr(755,root,root) %{_libdir}/libUnitTest++.so
%{_pkgconfigdir}/UnitTest++.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libUnitTest++.a
