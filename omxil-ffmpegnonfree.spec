Summary:	Non-free FFMpeg component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Nierozprowadzalny komponent FFMpeg dla implementacji Bellagio OpenMAX IL
Name:		omxil-ffmpegnonfree
Version:	0.1
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxffmpegnonfree-%{version}.tar.gz
# Source0-md5:	a2f652f51b149e23a0cc8f59a55a680e
URL:		http://omxil.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 0.5
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
Non-free FFmpeg component is a component for Bellagio OpenMAX IL that
uses non-free parts of FFMpeg libraries to decode/encode audio and
video.

It can:
- decode AMR audio
- encode AMR audio
- mux 3GP streams

Note: it expects FFMpeg built with the following options enabled:
shared, gpl, nonfree, swscale, libamr-nb, libvorbis.

%description -l pl.UTF-8
Nierozprowadzalny komponent FFMpeg to komponent dla implementacji
Bellagio OpenMAX IL, wykorzystujący elementy bibliotek FFMpeg nie
będące wolnodostępnym oprogramowaniem to dekodowania i kodowania
dźwięku i obrazu.

Komponent ten potrafi:
- dekodować dźwięk AMR
- kodować dźwięk AMR
- tworzyć strumienie 3GP

%prep
%setup -q -n libomxffmpegnonfree-%{version}

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomxffmpegnonfree.so*
