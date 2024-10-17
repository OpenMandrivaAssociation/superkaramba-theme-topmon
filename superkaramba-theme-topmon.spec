%define base_name       superkaramba-theme
%define theme_name      topmon
%define name            %{base_name}-%{theme_name}
%define version         0.3
%define release         7

Name:	 %{name}
Version: %{version}
Release: %{release}
Summary: Monitoring theme for superkaramba
License: GPL
Group:   Monitoring
Source:  %{theme_name}.tar.bz2
URL:     https://kde-look.org/content/show.php?content=21482
Requires: superkaramba >= 0.35
Requires: python
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
This is a superkaramba theme which is a desktop applet 
that displays system information.


%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{theme_name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/apps/superkaramba/themes/%{theme_name}
cp -rf * %buildroot/%{_datadir}/apps/superkaramba/themes/%{theme_name} 


%clean
rm -rf $RPM_BUILD_ROOT

%post 
if [ $1 = 1 ]; then
echo "THEME path=%{theme_name}/%{theme_name}.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
fi

%postun
if [ $1 = 0 ]; then
cat %{_datadir}/apps/superkaramba/themes/default.theme | grep -v "%{theme_name}" > %{_datadir}/apps/superkaramba/themes/default.theme
exit 0
fi


%files
%defattr(-,root,root)
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3-6mdv2010.0
+ Revision: 434193
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-5mdv2009.0
+ Revision: 261272
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-4mdv2009.0
+ Revision: 253762
- rebuild

* Sun Mar 02 2008 Nicolas Lécureuil <neoclust@mandriva.org> 0.3-2mdv2008.1
+ Revision: 177561
- [BUGFIX] Fix uninstall ( thanks misc) (Bug #22642)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3-1mdv2008.1
+ Revision: 128073
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Import superkaramba-theme-topmon





* Sun Mar 06 2005 Sebastien Savarin <plouf@mandrake.org> 0.3-1mdk
- initial release
