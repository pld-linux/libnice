Summary:	The GLib ICE implementation
Name:		libnice
Version:	0.0.11
Release:	1
License:	LGPL v2 and MPL v1.1
Group:		Libraries
Source0:	http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	9e6f6b0b781b747e49df2160cbb29f83
URL:		http://nice.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gstreamer-devel >= 0.10.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gupnp-igd-devel >= 0.1.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE). It provides GLib-based
library and GStreamer elements.

ICE is useful for applications that want to establish peer-to-peer UDP
data streams. It automates the process of traversing NATs and provides
security against some attacks.

Existing standards that use ICE include the Session Initiation
Protocol (SIP) and Jingle, XMPP extension for audio/video calls.

%package devel
Summary:	Header files for libnice library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnice
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.10.0

%description devel
Header files for libnice library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnice.

%package static
Summary:	Static libnice library
Summary(pl.UTF-8):	Statyczna biblioteka libnice
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnice library.

%description static -l pl.UTF-8
Statyczna biblioteka libnice.

%package apidocs
Summary:	libnice library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libnice
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libnice library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libnice.

%prep
%setup -q

%build
mkdir m4
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/stunbdc
%attr(755,root,root) %{_bindir}/stund
%attr(755,root,root) %{_libdir}/libnice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnice.so.0
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstnice.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnice.so
%{_libdir}/libnice.la
%{_includedir}/nice
%{_includedir}/stun
%{_pkgconfigdir}/nice.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnice.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libnice
