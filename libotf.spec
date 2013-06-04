%define	major	0
%define	libname %mklibname otf %{major}
%define	devname %mklibname -d otf
%define staticname %mklibname -d -s otf

Name:           libotf
Summary:        Library for handling OpenType fonts
Version:        0.9.13
Release:        1
Group:		System/Internationalization
License:	LGPLv2+
URL:		http://www.m17n.org/libotf/
Source0:	http://savannah.c3sl.ufpr.br/m17n/libotf-%version.tar.gz
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

%package -n	%{staticname}
Summary:	Static library for %{name}
Group:		Development/C
Requires:	%{devname} = %EVRD

%description -n %{staticname}
Static library for %{name}

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}otf0-devel

%description -n	%{devname}
Headers of %{name} for development.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files tools
%{_bindir}/otf*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/libotf-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/lib*.pc

%files -n %{staticname}
%{_libdir}/lib*.a
