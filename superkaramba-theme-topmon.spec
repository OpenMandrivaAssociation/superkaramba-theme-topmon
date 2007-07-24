%define base_name       superkaramba-theme
%define theme_name      topmon
%define name            %{base_name}-%{theme_name}
%define version         0.3
%define release         1mdk

Name:	 %{name}
Version: %{version}
Release: %{release}
Summary: Monitoring theme for superkaramba
License: GPL
Group:   Monitoring
Source:  %{theme_name}.tar.bz2
URL:     http://kde-look.org/content/show.php?content=21482
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
fi


%files
%defattr(-,root,root)
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*
