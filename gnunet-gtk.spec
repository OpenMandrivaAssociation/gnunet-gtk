%define name gnunet-gtk
%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

%define pre pre2

Name:		%{name}
Version:        0.9.0
Release:        %mkrel 0.%{pre}.1
Source:		http://gnunet.org/download/%{name}-%{version}%{pre}.tar.gz
License:	GPLv2+
Summary:	GNUnet GTK user interface
Group:		Networking/File transfer
URL:		http://gnunet.org/
BuildRequires:	gnunet-devel = %{version}
BuildRequires:	gtk+2-devel
BuildRequires:	libextractor-devel
BuildRequires:	libgksu-devel
#BuildRequires:	libglade2-devel
BuildRequires:	glade3-devel
Requires:	gnunet

%description
This is the GNUnet GTK user interface. GNUnet is a framework for secure
peer-to-peer networking that does not use any centralized or otherwise
trusted services.

%prep
%setup -q -n %{name}-%{version}%{pre}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#{__install} -d %{buildroot}%{_iconsdir}
#{__install} -m 644 pixmaps/gnunet_logo.png %{buildroot}%{_iconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc README AUTHORS ABOUT-NLS ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*

