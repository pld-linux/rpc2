Summary:	RPC2 library
Name:		rpc2
Version:	1.5
Release:	1
License:	GPL
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
BuildRequires:	lwp-devel
Source:		ftp://ftp.coda.cs.cmu.edu/pub/coda/src/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RPC2 library.

%package devel
Summary:	RPC2 library development files
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Headers and libraries for developing programs using the RPC2 library.

%package static
Summary:	RPC2 static library development files
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the RPC2 library.

%prep
%setup -q

%build
%configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(755,root,root,755)
%{_bindir}/filcon
%{_libdir}/libfail.so.1.0.0
%{_libdir}/librpc2.so.1.1.1
%{_libdir}/libse.so.1.0.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rp2gen
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/rpc2/errors.h
%{_includedir}/rpc2/errorsdefs.h
%{_includedir}/rpc2/fail.h
%{_includedir}/rpc2/fcon.h
%{_includedir}/rpc2/multi.h
%{_includedir}/rpc2/rpc2.h
%{_includedir}/rpc2/se.h
%{_includedir}/rpc2/sftp.h

%files static
%defattr(644,root,root,755)
%{_libdir}/librpc2.a
%{_libdir}/libfail.a
%{_libdir}/libse.a
