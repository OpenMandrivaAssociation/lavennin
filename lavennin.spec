
%define name	lavennin
%define version	20041119
%define rel	4
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20041119-4mdv2011.0
+ Revision: 620054
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 20041119-3mdv2010.0
+ Revision: 429702
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 20041119-2mdv2008.1
+ Revision: 136535
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Anssi Hannula <anssi@mandriva.org> 20041119-2mdv2008.0
+ Revision: 77449
- rebuild
- Import lavennin



* Sat Aug  5 2006 Anssi Hannula <anssi@mandriva.org> 20041119-1mdv2007.0
- initial Mandriva release
