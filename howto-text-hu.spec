%define format	text-hu
%define format2	TEXT/hu
%define	format3 text

%define version 2006
%define release %mkrel 6

Summary:	HOWTO documents (%{format3} format) from the Linux Documentation Project
Name:		howto-%{format}
Version: 	%version
Release: 	%release
Group:		Books/Howtos
Source0:	howto-%{format}.tar.bz2
Url:		http://www.kde.hu/mlp/hogyanok/
License:	GPL
BuildRoot:	%{_tmppath}/howto-%{format}-root
BuildArchitectures: noarch
Requires:   locales-hu howto-utils
BuildRequires:  howto-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

Install this package if you'd like to be able to access the Linux
HOWTO documentation from your own system.

%prep 
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
cd $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
bzcat %{SOURCE0} | tar xv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2006-6mdv2011.0
+ Revision: 619432
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2006-5mdv2010.0
+ Revision: 429419
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2006-4mdv2009.0
+ Revision: 247012
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 2006-3mdv2009.0
+ Revision: 239612
- rebuild
- better description

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2006-1mdv2008.1
+ Revision: 126817
- kill re-definition of %%buildroot on Pixel's request
- import howto-text-hu


* Thu Dec 15 2005 Lenny Cartier <lenny@mandriva.com> 2006-1mdk
- rebuild

* Thu Oct 09 2003 Lenny Cartier <lenny@mandrakesoft.com> 9.2-1mdk
- updated

* Fri Sep 13 2002 Lenny Cartier <lenny@mandrakesoft.com> 9.0-1mdk
- Update

* Thu Sep 06 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-1mdk
- Updated: Thu Sep 06 2001
- Add Require on locale-hu

* Thu Mar 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 8.0-1mdk
- rebuild

* Thu Nov 09 2000 Lenny Cartier <lenny@mandrakesoft.com> 7.2-1mdk
- used srpm from Andras TIMAR <timar@linux-mandrake.com> :
	- first Mandrake RPM

