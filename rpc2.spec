Summary:	RPC2 library
Name:		rpc2
Version:	cvs20001115
Release:	1
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	%{name}-%{version}.tgz
BuildRequires:	flex
BuildRequires:	lwp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RPC2 library.

%package devel
Summary:	RPC2 library development files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Headers and libraries for developing programs using the RPC2 library.

%package static
Summary:	RPC2 static library development files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the RPC2 library.

%prep
%setup -q -n rpc2

%build
touch ChangeLog README AUTHORS
autoheader
aclocal
libtoolize
automake --copy --add-missing
autoconf
%configure --prefix=%{_prefix}
%{__make} OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS INSTALL COPYING
%attr(755,root,root) %{_bindir}/filcon
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rp2gen
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/rpc2

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
