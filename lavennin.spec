
%define name	lavennin
%define version	20041119
%define rel	3
%define release	%mkrel %rel

Summary:	Converts written Finnish text to a readable form
Name:		%name
Version:	%version
Release:	%release
License:	LGPL
Group:		Sound
URL:		http://phon.joensuu.fi/suopuhe/
Source:		http://www.ling.helsinki.fi/suopuhe/download/%name-%version.tar.bz2
Patch0:		lavennin-paths.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
# per Mandriva locale-specific package policy:
Requires:	locales-fi

%description
Lavennin converts numbers, abbreviations and other such non-readable
strings found in usual written Finnish text to a readable form.
Therefore only the grafem-fonem conversion is left for the speech
synthesizer. Lavennin can also be used to nativisate
foreign-originated words.

%prep
%setup -q -n %name
%patch0 -p1

sed -i 's,@LAVENNINDATADIR@,\"%{_datadir}/%{name}\",' bin/lavennin

%install
rm -rf %{buildroot}

install -d -m755 %{buildroot}%{_bindir}
install -m755 bin/lavennin %{buildroot}%{_bindir}

install -d -m755 %{buildroot}%{_datadir}/%{name}
install -m644 data/*.txt %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc man/*.shtml
%{_bindir}/lavennin
%{_datadir}/%{name}
