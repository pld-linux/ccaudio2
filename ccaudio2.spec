Summary:	GNU ccAudio2 - a C++ class framework for processing audio files
Summary(pl):	GNU ccAudio2 - klasa C++ do przetwarzania plik�w d�wi�kowych
Name:		ccaudio2
Version:	0.7.7
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/ccaudio/%{name}-%{version}.tar.gz
# Source0-md5:	69c8ac35070181e4c1b01ec1ede5087e
URL:		http://www.gnu.org/software/ccaudio/
BuildRequires:	libgsm-devel
BuildRequires:	libstdc++-devel
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

%description -l pl
Pakiet GNU ccAudio oferuje przeno�n� klas� C++ do tworzenia aplikacji
zmieniaj�cych strumienie d�wi�kowe i r�ne formaty plik�w na dyskach.
Aktualnie obs�uguje pliki .au, .wav (RIFF) i r�ne formaty kodowania
.raw w systemach zgodnych z POSIX oraz Win32, mo�e si� jednak
rozrosn��, aby zosta� bibliotek� og�lnego u�ytku do d�wi�ku i kart
d�wi�kowych. Ostatnio zosta�a dodana obs�uga sterowania urz�dzeniami
z p�ytami CD Audio, jak tak�e obs�uga kodek�w i innych og�lnych us�ug
przetwarzaj�cych d�wi�k.

%package devel
Summary:	Header files for ccaudio2 library
Summary(pl):	Pliki nag��wkowe biblioteki ccaudio2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ccaudio2 library.

%description devel -l pl
Pliki nag��wkowe biblioteki ccaudio2.

%package static
Summary:	Static ccaudio2 library
Summary(pl):	Statyczna biblioteka ccaudio2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ccaudio2 library.

%description static -l pl
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/%{name}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cc++
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
