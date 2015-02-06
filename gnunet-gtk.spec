%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	GNUnet GTK user interface
Name:		gnunet-gtk
Version:	0.10.0
Release:	2
License:	GPLv2+
Group:		Networking/File transfer
Url:		http://gnunet.org/
Source0:	http://gnunet.org/download/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gladeui-1.0)
BuildRequires:	pkgconfig(gnunetcore) = %{version}
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libextractor)
BuildRequires:	pkgconfig(libgksu2)
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

%package -n %{devname}
Summary:	GNUnet GTK development files
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{name}-devel < 0.10.0
Conflicts:	%{name}-devel < 0.10.0

%description -n %{devname}
This is the GNUnet GTK user interface. GNUnet is a framework for secure
peer-to-peer networking that does not use any centralized or otherwise
trusted services.

This package contains files required for development only.

%files -n %{devname}
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

