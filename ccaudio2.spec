Summary:	GNU ccAudio2 - a C++ class framework for processing audio files
Summary(pl.UTF-8):	GNU ccAudio2 - klasa C++ do przetwarzania plików dźwiękowych
Name:		ccaudio2
Version:	2.1.3
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/ccaudio/%{name}-%{version}.tar.gz
# Source0-md5:	a085ae863cead3da30387d2bc29bbd63
URL:		http://www.gnu.org/software/ccaudio/
BuildRequires:	libgsm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	speex-devel
BuildRequires:	ucommon-devel >= 6.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU ccAudio package offers a highly portable C++ class framework
for developing applications which manipulate audio streams and various
disk based audio file formats. At the moment ccaudio is primarly a
class framework for handling .au, .wav (RIFF), and various .raw audio
encoding formats under POSIX and Win32 systems, though it may expand
to become a general purpose audio and soundcard support library.
Support for controlling CD audio devices has recently been added as
well as support for codecs and other generic audio processing
services.

%description -l pl.UTF-8
Pakiet GNU ccAudio oferuje przenośną klasę C++ do tworzenia aplikacji
zmieniających strumienie dźwiękowe i różne formaty plików na dyskach.
Aktualnie obsługuje pliki .au, .wav (RIFF) i różne formaty kodowania
.raw w systemach zgodnych z POSIX oraz Win32, może się jednak
rozrosnąć, aby zostać biblioteką ogólnego użytku do dźwięku i kart
dźwiękowych. Ostatnio została dodana obsługa sterowania urządzeniami
z płytami CD Audio, jak także obsługa kodeków i innych ogólnych usług
przetwarzających dźwięk.

%package devel
Summary:	Header files for ccaudio2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ccaudio2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgsm-devel
Requires:	libstdc++-devel
Requires:	speex-devel
Requires:	ucommon-devel >= 6.0.0

%description devel
Header files for ccaudio2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ccaudio2.

%package static
Summary:	Static ccaudio2 library
Summary(pl.UTF-8):	Statyczna biblioteka ccaudio2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ccaudio2 library.

%description static -l pl.UTF-8
Statyczna biblioteka ccaudio2.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libccaudio2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README SUPPORT THANKS TODO
%attr(755,root,root) %{_bindir}/audiotool
%attr(755,root,root) %{_bindir}/tonetool
%attr(755,root,root) %{_libdir}/libccaudio2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libccaudio2.so.2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tones.conf
%{_mandir}/man1/audiotool.1*
%{_mandir}/man1/tonetool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libccaudio2.so
%{_includedir}/ccaudio2.h
%{_pkgconfigdir}/ccaudio2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libccaudio2.a
