Summary:	The GLib ICE (Interactive Connectivity Establishment) implementation
Summary(pl.UTF-8):	Implementacja ICE (Interactive Connectivity Establishment) oparta o GLib
Name:		libnice
Version:	0.1.2
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	1914dd98380dd68632d3d448cc23f1e8
URL:		http://nice.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.13
BuildRequires:	gstreamer-devel >= 0.10.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gupnp-igd-devel >= 0.1.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.13
Requires:	gupnp-igd >= 0.1.2
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
Establishment) wg szkicu IETF. Udostępnia bibliotekę opartą na
GLibie oraz elementy GStreamera.

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
Requires:	glib2-devel >= 1:2.13
Requires:	gupnp-igd-devel >= 0.1.2

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
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

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
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstnice.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnice.so
%{_includedir}/nice
%{_includedir}/stun
%{_pkgconfigdir}/nice.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnice.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libnice
