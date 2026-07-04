Summary:	Library to pack up hard disk files and directories into a ISO 9660 disk image
Summary(pl.UTF-8):	Biblioteka do pakowania plików i katalogów w obrazy ISO 9660
Name:		libisofs
Version:	1.5.8.pl02
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	48150014510f8e65de66cb687ff63957
Patch0:		%{name}-pc.patch
URL:		https://dev.lovelyhq.com/libburnia/web/wiki
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	libjte-devel >= 2.0.0
BuildRequires:	zlib-devel
Requires:	libjte >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
libisofs is the library to pack up hard disk files and directories
into a ISO 9660 disk image.

%description -l pl.UTF-8
libisofs to biblioteka do pakowania plików i katalogów z twardego
dysku w obrazy ISO 9660.

%package devel
Summary:	Header files for libisofs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libisofs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	acl-devel
Requires:	attr-devel
Requires:	libjte-devel >= 2.0.0
Requires:	zlib-devel

%description devel
Header files for libisofs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libisofs.

%package static
Summary:	Static libisofs library
Summary(pl.UTF-8):	Statyczna biblioteka libisofs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libisofs library.

%description static -l pl.UTF-8
Statyczna biblioteka libisofs.

%prep
%setup -q -n %{name}-1.5.8
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config (with patch)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libisofs.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT ChangeLog NEWS README Roadmap TODO
%{_libdir}/libisofs.so.*.*.*
%ghost %{_libdir}/libisofs.so.6

%files devel
%defattr(644,root,root,755)
%doc doc/Tutorial
%{_libdir}/libisofs.so
%{_includedir}/libisofs
%{_pkgconfigdir}/libisofs-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libisofs.a
