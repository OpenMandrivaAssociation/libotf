%define	major	0
%define	libname %mklibname otf %{major}
%define	devname %mklibname -d otf

Summary:        Library for handling OpenType fonts
Name:           libotf
Version:        0.9.13
Release:        2
Group:		System/Internationalization
License:	LGPLv2+
Url:		http://www.m17n.org/libotf/
Source0:	http://savannah.c3sl.ufpr.br/m17n/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xt)

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

%description	tools
Tools from %{name}

%package -n	%{libname}
Summary:	Main OpenType library
Group:		System/Internationalization
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Libotf library.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Headers of %{name} for development.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files tools
%{_bindir}/otf*

%files -n %{libname}
%{_libdir}/libotf.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/libotf-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/lib*.pc

