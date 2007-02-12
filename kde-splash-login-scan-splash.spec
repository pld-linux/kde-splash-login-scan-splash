
%define		_splash		login-scan-splash

Summary:	login-scan 'splash' KDE splash screen
Summary(pl.UTF-8):   Ekran startowy KDE login-scan 'splash'
Name:		kde-splash-%{_splash}
Version:	0.2
Release:	2
License:	check first if it's GPL
Group:		X11/Amusements
Source0:	http://www.rokkford.de/loginscansplash/%{_splash}.tar.gz
# Source0-md5:	e0078d6de0561ffdda9ee7cba0a0af53
URL:		http://kde-look.org/content/show.php?content=26888
Requires:	kde-splash-moodin
Requires:	kdebase-desktop
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
login-scan 'splash' KDE splash screen.

%description -l pl.UTF-8
Ekran startowy KDE login-scan 'splash'.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

install %{_splash}/*.png $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install %{_splash}/Theme.rc $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#doc %{_splash}/README %{_splash}/THEMEOPTIONS
%{_datadir}/apps/ksplash/Themes/%{_splash}
