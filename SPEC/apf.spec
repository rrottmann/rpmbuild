Summary: Adventure PHP Framework
Name: apf
Version: 1.17
Release: 2%{?dist}
License: GPLv3 and LGPLv3
Group: Applications/System
URL: http://www.adventure-php-framework.org
Source: http://files.adventure-php-framework.org/1.17/download/apf-demopack-1.17-2013-04-13-1126-php5.tar.gz
Source1: adventure-php-framework.conf
BuildArch: noarch

BuildRequires: dos2unix

Requires: mod_php, php-mysql, httpd
Requires(post): policycoreutils-python
Requires(postun): policycoreutils-python

%description
The Adventure PHP Framework is used to rapidly create
enterprise ready web applications or modules, that are
fast, secure and reusable. It includes approved
development tools to solve standard problems and
implement pattern related applications. 

%prep

%setup -c -q

%install
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/doc
mkdir -p %{buildroot}%{_datadir}/doc/adventure-php-framework
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
mkdir -p %{buildroot}%{_sysconfdir}/adventure-php-framework/apps/
mkdir -p %{buildroot}%{_sharedstatedir}/adventure-php-framework/{crash,devel,prod}
cp -av . %{buildroot}%{_datadir}/adventure-php-framework
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/
# remove zero-length files
find %{buildroot} -size 0 -delete
# convert source files that were not created on Linux
find %{buildroot}%{_datadir}/adventure-php-framework/ -type f -iname "*.php" -exec dos2unix {} &>/dev/null \;
find %{buildroot}%{_datadir}/adventure-php-framework/ -type f -iname "*.txt" -exec dos2unix {} &>/dev/null \;
find %{buildroot}%{_datadir}/adventure-php-framework/ -type f -iname "*.js" -exec dos2unix {} &>/dev/null \;
find %{buildroot}%{_datadir}/doc/adventure-php-framework/ -type f -iname "*.txt" -exec dos2unix {} &>/dev/null \;
# move files to honour the file hierarchy standard
mv %{buildroot}%{_datadir}/adventure-php-framework/apps/sandbox %{buildroot}%{_sharedstatedir}/adventure-php-framework/
mv %{buildroot}%{_datadir}/adventure-php-framework/*.txt %{buildroot}%{_datadir}/doc/adventure-php-framework/
mv %{buildroot}%{_datadir}/adventure-php-framework/apps/config %{buildroot}%{_sysconfdir}/adventure-php-framework/apps/
ln -s %{_sysconfdir}/adventure-php-framework/apps/config %{buildroot}%{_datadir}/adventure-php-framework/apps/ 
ln -s %{_sharedstatedir}/adventure-php-framework/{sandbox,crash,devel,prod} %{buildroot}%{_datadir}/adventure-php-framework/apps/

%post
semanage fcontext -a -t httpd_sys_content_t %{_datadir}/adventure-php-framework 2>/dev/null
restorecon -R %{_datadir}/adventure-php-framework

%postun
if [ $1 -eq 0 ]; then  # final removal
semanage fcontext -d -t httpd_sys_content_t %{_datadir}/adventure-php-framework/ 2>/dev/null || :
fi

%clean

%files
%{_datadir}/adventure-php-framework/
%{_sharedstatedir}/adventure-php-framework/
%doc %{_datadir}/doc/adventure-php-framework/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/adventure-php-framework.conf
%config(noreplace) %{_sysconfdir}/adventure-php-framework/

%changelog
* Mon Oct 21 2013 Reiner Rottmann <reiner@rottmann.it> 1.17-2
- Incorporated improvements from bz#734248 comment15

* Mon Oct 21 2013 Reiner Rottmann <reiner@rottmann.it> 1.17-1
- Using latest apf 1.17

* Tue Nov 20 2012 Reiner Rottmann <reiner@rottmann.it> 1.16-1
- Using latest apf 1.16
- Adapted spec file for Fedora 18

* Tue Jul 3 2012 Reiner Rottmann <reiner@rottmann.it> 1.15-2
- Incorporated improvements from bz#734248
- Cleanup of spec file
- Removed macros for cp and mv
- Removed restart of httpd
- Removed php and mysql dependency
- Changed target dirs
- Added dos2unix as build prerequisite

* Sat Jun 30 2012 Reiner Rottmann <reiner@rottmann.it> 1.15-1
- Using latest apf 1.15
- Adapted spec file for Fedora 17
- Added SELinux context
- Removing zero-length files

* Sat Aug  27 2011 Reiner Rottmann <reiner@rottmann.it> 1.13-1
- First packaged for Fedora 15
