Summary:	Library to pack up hard disk files and directories into a ISO 9660 disk image
Summary(pl.UTF-8):	Biblioteka do pakowania plików i katalogów w obrazy ISO 9660
Name:		libisofs
Version:	1.5.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	db86f85c639798b082ab967edfb9ce82
URL:		http://libburnia-project.org/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	libjte-devel >= 1.0.0
BuildRequires:	zlib-devel
Requires:	libjte >= 1.0.0
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
Requires:	libjte-devel >= 1.0.0
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
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# *.la kept, dependencies are missing in .pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT ChangeLog NEWS README Roadmap TODO
%attr(755,root,root) %{_libdir}/libisofs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libisofs.so.6

%files devel
%defattr(644,root,root,755)
%doc doc/Tutorial
%attr(755,root,root) %{_libdir}/libisofs.so
%{_libdir}/libisofs.la
%{_includedir}/libisofs
%{_pkgconfigdir}/libisofs-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libisofs.a
