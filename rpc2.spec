Summary:	RPC2 library
Summary(pl.UTF-8):	Biblioteka RPC2
Summary(pt_BR.UTF-8):	Biblioteca RPC2
Name:		rpc2
Version:	2.6.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/rpc2/src/%{name}-%{version}.tar.gz
# Source0-md5:	458a4c4473ba780cc902bef24fe5da32
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

%description -l pl.UTF-8
Biblioteka RPC2.

%description -l pt_BR.UTF-8
Biblioteca RPC2. Utilizada pelo sistema de arquivos distribuído Coda.

%package devel
Summary:	RPC2 library development files
Summary(pl.UTF-8):	Pliki dla programistów używających biblioteki RPC2
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para desenvolvimento com a RPC2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	librpc21-devel

%description devel
Headers for developing programs using the RPC2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów z użyciem RPC2.

%description devel -l pt_BR.UTF-8
Biblioteca RPC2. Utilizada pelo sistema de arquivos distribuído Coda.

%package static
Summary:	RPC2 static library development files
Summary(pl.UTF-8):	Biblioteka statyczna RPC2
Summary(pt_BR.UTF-8):	Biblioteca estática para desenvolvimento com a RPC2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for developing programs using the RPC2 library.

%description static -l pl.UTF-8
Statyczne biblioteki RPC2.

%description static -l pt_BR.UTF-8
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
