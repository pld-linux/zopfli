Summary:	Compression library to perform very good, but slow, deflate or zlib compression
Summary(pl.UTF-8):	Biblioteka wykonująca bardzo dobrą, ale wolną kompresję deflate lub zlib
Name:		zopfli
Version:	1.0.3
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/google/zopfli/releases
Source0:	https://github.com/google/zopfli/archive/%{name}-%{version}.tar.gz
# Source0-md5:	ebc042f0c13f7e367e72d2b96be1a4c0
Patch0:		%{name}-link.patch
URL:		https://github.com/google/zopfli
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zopfli is a compression library programmed in C to perform very good,
but slow, deflate or zlib compression.

%description -l pl.UTF-8
Zopfli to napisana w C biblioteka kompresująca do wykonywania bardzo
dobrej, ale wolnej kompresji deflate lub zlib.

%package devel
Summary:	Header files for Zopfli library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Zopfli
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Zopfli library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Zopfli.

%package png
Summary:	Zopfli PNG compression library
Summary(pl.UTF-8):	Biblioteka Zopfli do kompresji plików PNG
Group:		Libraries

%description png
Zopfli PNG compression library.

%description png -l pl.UTF-8
Biblioteka Zopfli do kompresji plików PNG.

%package png-devel
Summary:	Header files for Zopfli PNG library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Zopfli PNG
Group:		Development/Libraries
Requires:	%{name}-png = %{version}-%{release}

%description png-devel
Header files for Zopfli PNG library.

%description png-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Zopfli PNG.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

%build
%{__make} -j1 libzopfli libzopflipng zopfli zopflipng \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -W -Wall -Wextra -ansi -pedantic" \
	CXXFLAGS="%{rpmcxxflags} %{rpmcppflags} -W -Wall -Wextra -ansi -pedantic" \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install libzopfli.so.%{version} libzopflipng.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install zopfli zopflipng $RPM_BUILD_ROOT%{_bindir}
cp -p src/zopfli/zopfli.h src/zopflipng/zopflipng_lib.h $RPM_BUILD_ROOT%{_includedir}

/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}
ln -sf libzopfli.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzopfli.so
ln -sf libzopflipng.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzopflipng.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	png -p /sbin/ldconfig
%postun	png -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README README.zopflipng
%attr(755,root,root) %{_bindir}/zopfli
%attr(755,root,root) %{_libdir}/libzopfli.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzopfli.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzopfli.so
%{_includedir}/zopfli.h

%files png
%defattr(644,root,root,755)
%doc README.zopflipng
%attr(755,root,root) %{_bindir}/zopflipng
%attr(755,root,root) %{_libdir}/libzopflipng.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzopflipng.so.1

%files png-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzopflipng.so
%{_includedir}/zopflipng_lib.h
