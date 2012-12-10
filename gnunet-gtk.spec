%define name gnunet-gtk
%define major 1
%define libname %mklibname %{name} %{major}

Name:		%{name}
Version:        0.9.1
Release:        1
Source0:	http://gnunet.org/download/%{name}-%{version}.tar.gz
License:	GPLv2+
Summary:	GNUnet GTK user interface
Group:		Networking/File transfer
URL:		http://gnunet.org/
BuildRequires:	gnunet-devel = %{version}
BuildRequires:	gtk+2-devel
BuildRequires:	libextractor-devel
BuildRequires:	libgksu-devel
BuildRequires:	glade3-devel
Requires:	gnunet

%description
This is the GNUnet GTK user interface. GNUnet is a framework for secure
peer-to-peer networking that does not use any centralized or otherwise
trusted services.

%files -f %{name}.lang
%doc README AUTHORS ABOUT-NLS ChangeLog
%{_bindir}/gnunet-*
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/gnunet-*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*

#------------------------------------------------------------------------------

%package -n %{libname}
Summary:	GNUnet GTK library
Group:		System/Libraries

%description -n %{libname}
This is the GNUnet GTK user interface. GNUnet is a framework for secure
peer-to-peer networking that does not use any centralized or otherwise
trusted services.

This package contains lib%{name} shared library.

%files -n %{libname}
%{_libdir}/libgnunetgtk.so.%{major}*

#------------------------------------------------------------------------------

%package devel
Summary:        GNUnet GTK development files
Group:          System/Libraries
Requires:	%{libname} = %{version}

%description devel
This is the GNUnet GTK user interface. GNUnet is a framework for secure
peer-to-peer networking that does not use any centralized or otherwise
trusted services.

This package contains files required for development only.

%files devel
%doc README AUTHORS ABOUT-NLS ChangeLog
%{_includedir}/%{name}/gnunet_gtk.h
%{_libdir}/libgnunetgtk.so

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}


%changelog
* Mon Jan 16 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.1-1
+ Revision: 761829
- new tarball
- new version 0.9.1

* Thu Aug 11 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.0-0.pre2.1
+ Revision: 693964
- imported package gnunet-gtk


* Thu Aug 11 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.9.0-0.pre2.1mdv2011.0
- New version 0.9.0pre2
- Port to 2011

* Thu Apr 03 2008 Anssi Hannula <anssi@zarb.org> 0.7.3-1plf2008.1
- add to PLF
- drop duplicate menu entry
- buildrequires libglade2

* Fri Mar 21 2008 Nicolas Vigier <boklm@mars-attacks.org> 0.7.3-1mdv2008.1
- first version
