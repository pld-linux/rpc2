Summary:	RPC2 library
Summary(pl):	Biblioteka RPC2
Summary(pt_BR):	Biblioteca RPC2
Name:		rpc2
Version:	2.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/rpc2/src/%{name}-%{version}.tar.gz
# Source0-md5:	2609ed0e6ad81b77fe7613af1de40b97
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	lwp-devel
BuildRequires:	readline-devel
Obsoletes:	librpc21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The RPC2 library. RPC2 Library, used with the coda file system.

%description -l pl
Biblioteka RPC2.

%description -l pt_BR
Biblioteca RPC2. Utilizada pelo sistema de arquivos distribuído Coda.

%package devel
Summary:	RPC2 library development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych biblioteki RPC2
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para desenvolvimento com a RPC2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	librpc21-devel

%description devel
Headers for developing programs using the RPC2 library.

%description devel -l pl
Pliki nag³ówkowe do tworzenia programów z u¿yciem RPC2.

%description devel -l pt_BR
Biblioteca RPC2. Utilizada pelo sistema de arquivos distribuído Coda.

%package static
Summary:	RPC2 static library development files
Summary(pl):	Biblioteka statyczna RPC2
Summary(pt_BR):	Biblioteca estática para desenvolvimento com a RPC2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for developing programs using the RPC2 library.

%description static -l pl
Statyczne biblioteki RPC2.

%description static -l pt_BR
Biblioteca RPC2. Utilizada pelo sistema de arquivos distribuído Coda.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README*
%attr(755,root,root) %{_bindir}/filcon
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rp2gen
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/rpc2

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
