#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	The GLib ICE (Interactive Connectivity Establishment) implementation
Summary(pl.UTF-8):	Implementacja ICE (Interactive Connectivity Establishment) oparta o GLib
Name:		libnice
Version:	0.1.15
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	https://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	5f58f305d23158651ab509b25420d353
URL:		https://nice.freedesktop.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.12
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.48
BuildRequires:	gnutls-devel >= 2.12
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gupnp-igd-devel >= 0.2.4
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.48
Requires:	gnutls-libs >= 2.12
Requires:	gupnp-igd >= 0.2.4
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

%description -l pl.UTF-8
libnice to implementacja standardu ICE (Interactive Connectivity
Establishment) wg szkicu IETF. Udostępnia bibliotekę opartą na GLibie
oraz elementy GStreamera.

ICE służy aplikacjom chcącym tworzyć strumienie danych UDP
peer-to-peer. Automatyzuje proces przechodzenia przez NAT i
zabezpiecza przed pewnymi atakami.

Istniejące standardy wykorzystujące ICE obejmują protokoły SIP
(Session Initiation Protocol) oraz Jingle (rozszerzenie XMPP dla
połączeń audio/video).

%package devel
Summary:	Header files for libnice library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnice
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.48
Requires:	gnutls-devel >= 2.12
Requires:	gupnp-igd-devel >= 0.2.4

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
libnice library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libnice.

%package -n gstreamer-nice
Summary:	ICE source plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka źródła ICE dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= 1.0.0

%description -n gstreamer-nice
ICE source plugin for GStreamer.

%description -n gstreamer-nice -l pl.UTF-8
Wtyczka źródła ICE dla GStreamera.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-compile-warnings \
	--enable-gtk-doc \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir} \
	--without-gstreamer-0.10

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/stunbdc
%attr(755,root,root) %{_bindir}/stund
%attr(755,root,root) %{_libdir}/libnice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnice.so.10
%{_libdir}/girepository-1.0/Nice-0.1.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnice.so
%{_includedir}/nice
%{_includedir}/stun
%{_datadir}/gir-1.0/Nice-0.1.gir
%{_pkgconfigdir}/nice.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnice.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libnice

%files -n gstreamer-nice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstnice.so
