Summary:	RPC2 library
Summary(pl):	Biblioteka RPC2
Name:		rpc2
Version:	1.12
Release:	2
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/rpc2/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-LIBTOOL_LDFLAGS.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	lwp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RPC2 library.

%description -l pl
Biblioteka RPC2.

%package devel
Summary:	RPC2 library development files
Summary(pl):	Pliki dla programistów używających biblioteki RPC2
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers for developing programs using the RPC2 library.

%description devel -l pl
Pliki nagłówkowe do tworzenia programów z użyciem RPC2.

%package static
Summary:	RPC2 static library development files
Summary(pl):	Biblioteka statyczna RPC2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using the RPC2 library.

%description static -l pl
Statyczne biblioteki RPC2.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
autoheader
aclocal
automake --copy --add-missing
autoconf
%configure --prefix=%{_prefix}
%{__make} OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS.gz
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
