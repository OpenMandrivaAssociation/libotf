%define version 0.9.12
%define release %mkrel -c RC 1

%define major 0
%define libname %mklibname otf %{major}
%define develname %mklibname -d otf

Name:           libotf
Summary:        Library for handling OpenType fonts
Version:        %{version}
Release:        %{release}
Group:		System/Internationalization
License:	LGPLv2+
URL:		http://www.m17n.org/libotf/
Source0:	http://www.m17n.org/libotf/%{name}-%{version}RC.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	freetype2-devel
BuildRequires:	libx11-devel
BuildRequires:	libxaw-devel
BuildRequires:	libxt-devel

%description
The library "libotf" provides the following facilites:
- Read Open Type Layout Tables from OTF file (currently supported tables are:
  head, name, cmap, GDEF, GSUB, and GPOS)
- Convert a Unicode character sequence to a glyph code sequence by using the
  above tables.

The combination of libotf and the FreeType library realizes CTL (Complex Text
Layout) by OpenType fonts.*

%package	tools
Summary:	Utilities of OpenType library
Group:		System/Internationalization
Obsoletes:	%{name}-example
Requires:	%{libname} = %{version}

%description	tools
Example tool from %name

%package -n	%{libname}
Summary:	Main OpenType library
Group:		System/Internationalization
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Libotf library.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}otf0-devel

%description -n	%{develname}
Headers of %{name} for development.

%prep
%setup -qn %{name}-%{version}RC

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files tools
%defattr(-,root,root)
%doc COPYING
%{_bindir}/otf*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/libotf-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/lib*.pc
