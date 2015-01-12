%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           python-itools
Version:        0.75.1
Release:        1%{?dist}
Summary:        The itools library
Group:          Development/Languages
License:        GPLv1
URL:            http://www.hforge.org/itools
Source0:        http://download.hforge.org/itools/0.75/itools-0.75.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel
BuildRequires:  glib2-devel

%description
The itools library offers a collection of packages covering a wide
range of capabilities.  Including support for many file formats (XML,
CSV, HTML, etc.), a virtual file system (itools.fs), the simple
template language (STL), an index and search engine, and much more.

%prep
%setup -q -n itools-0.75.1

%build

%install
%{__python} setup.py install --root $RPM_BUILD_ROOT 

%files
%doc CREDITS.txt
%doc INSTALL.txt
%doc LICENSE.txt
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

%changelog
* Mon Jan 12 2015 Reiner Rottmann <reiner@rottmann.it> - 0.75.1-1
- Initial package
