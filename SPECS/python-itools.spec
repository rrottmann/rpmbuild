Name:           python-itools
Version:        0.75.1
Release:        2%{?dist}
Summary:        The itools library
Group:          Development/Languages
License:        GPLv1
URL:            http://www.hforge.org/itools
Source0:        http://download.hforge.org/itools/0.75/itools-0.75.1.tar.gz
Requires:       python-xappy
Requires:       python-pygit2
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-gudev

%description
The itools library offers a collection of packages covering a wide
range of capabilities.  Including support for many file formats (XML,
CSV, HTML, etc.), a virtual file system (itools.fs), the simple
template language (STL), an index and search engine, and much more.

%prep
%setup -q -n itools-0.75.1

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
find %{buildroot} \( -name *.[ch] -o -name *.cc -o -name .mailmap \) -delete

%files
%license LICENSE.txt
%doc CREDITS.txt
%doc INSTALL.txt
%doc README.txt
%doc RELEASE-0.75.0
%doc RELEASE-0.75.1
%doc UPGRADE-0.75.0
%{python_sitearch}/*
/usr/bin/idb-inspect.py
/usr/bin/igettext-build.py
/usr/bin/igettext-extract.py
/usr/bin/igettext-merge.py
/usr/bin/iodf-greek.py
/usr/bin/ipkg-build.py
/usr/bin/ipkg-copyright.py
/usr/bin/ipkg-docs.py
/usr/bin/ipkg-quality.py
/usr/bin/ipkg-update-locale.py
%exclude %{python_sitearch}/itools/CREDITS.txt
%exclude %{python_sitearch}/itools/INSTALL.txt
%exclude %{python_sitearch}/itools/LICENSE.txt
%exclude %{python_sitearch}/itools/README.txt
%exclude %{python_sitearch}/itools/version.txt
%exclude %{python_sitearch}/itools/workflow/HOWTO.txt
%exclude %{python_sitearch}/itools/workflow/TODO.txt

%changelog
* Tue Jan 27 2015 Reiner Rottmann <reiner@rottmann.it> - 0.75.1-2
- Modified spec file according bz#1181317

* Mon Jan 12 2015 Reiner Rottmann <reiner@rottmann.it> - 0.75.1-1
- Initial package
