%define version 0.9.12
%define release 3

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
Source0:	http://www.m17n.org/libotf/%{name}-%{version}.tar.gz
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
%setup -qn %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%clean

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
%{_libdir}/pkgconfig/lib*.pc


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.12-2mdv2011.0
+ Revision: 660275
- mass rebuild

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 0.9.12-1mdv2011.0
+ Revision: 582858
- 0.9.12 final

* Thu Sep 23 2010 Funda Wang <fwang@mandriva.org> 0.9.12-0.RC.1mdv2011.0
+ Revision: 580636
- new version 0.9.12 rc

* Tue Mar 30 2010 Funda Wang <fwang@mandriva.org> 0.9.11-1mdv2010.1
+ Revision: 528959
- update to new version 0.9.11

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.10-1mdv2010.1
+ Revision: 462090
- update to new version 0.9.10

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.9-2mdv2010.0
+ Revision: 425684
- rebuild

* Sat Mar 07 2009 Funda Wang <fwang@mandriva.org> 0.9.9-1mdv2009.1
+ Revision: 351207
- New version 0.9.9

* Thu Sep 04 2008 Thierry Vignaud <tv@mandriva.org> 0.9.8-1mdv2009.0
+ Revision: 280829
- new release

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-2mdv2009.0
+ Revision: 222947
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Jan 11 2008 Funda Wang <fwang@mandriva.org> 0.9.7-1mdv2008.1
+ Revision: 147842
- update to new version 0.9.7

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 21 2007 Funda Wang <fwang@mandriva.org> 0.9.6-1mdv2008.0
+ Revision: 54223
- New version


* Tue Jan 09 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.9.5-1mdv2007.0
+ Revision: 106765
- Import libotf

* Thu Dec 07 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.9.5-1mdv2007.1
- new release

* Wed Nov 16 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.9.4-1mdk
- new release

* Wed Feb 09 2005 Abel Cheung <deaddog@mandrake.org> 0.9.3-3mdk
- Another BuildRequires fix

* Sat Feb 05 2005 Abel Cheung <deaddog@mandrake.org> 0.9.3-2mdk
- Fix BuildRequires
- Examples can be useful, thus rename to libotf-tools
  (similar to freetype2-tools)
- Move libotf-config to devel subpackage

* Tue Dec 28 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.9.3-1mdk
- new release

* Tue Nov 09 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.2-1mdk
- fix description
- fix libification
- initial spec for mdk (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

