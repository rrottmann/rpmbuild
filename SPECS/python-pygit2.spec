%global pkgname pygit2

Name:           python-%{pkgname}
Version:        0.22.0
Release:        1%{?dist}
Summary:        Python 2.x bindings for libgit2
URL:            http://www.pygit2.org
Source:         http://pypi.python.org/packages/source/p/%{pkgname}/%{pkgname}-%{version}.tar.gz
License:        GPLv2 with linking exception
BuildRequires:  libgit2-devel
BuildRequires:  openssl-devel
BuildRequires:  python-cffi
BuildRequires:  python2-devel
BuildRequires:  python-nose
BuildRequires:  python-setuptools

Requires:       python-cffi

#Patch0:         0001-Remove-remote-calling-unit-tests.patch

%description
pygit2 is a set of Python bindings to the libgit2 library, which implements 
the core of Git. Pygit2 works with Python 2.7, 3.1, 3.2, 3.3 and 3.4.


%package -n     python3-%{pkgname}
Summary:        Python 3.x bindings for libgit2
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools

Requires:       python3-cffi

%description -n python3-%{pkgname}
pygit2 is a set of Python bindings to the libgit2 library, which implements 
the core of Git. Pygit2 works with Python 2.7, 3.1, 3.2, 3.3 and 3.4.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  python-sphinx
Requires:       %{name} = %{version}-%{release}

%description    doc
Documentation for %{name}.


%prep
%setup -qn %{pkgname}-%{version}

#%patch0 -p1

rm -rf %{py3dir}
cp -a . %{py3dir}


%build
CFLAGS="%{optflags}" %{__python2} setup.py build
make -C docs html

pushd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py build
popd


%install
%{__python2} setup.py install --prefix=%{_prefix} -O1 --skip-build --root=%{buildroot}
pushd %{py3dir}
%{__python3} setup.py install --prefix=%{_prefix} -O1 --skip-build --root=%{buildroot}
popd
find %{_builddir} -name '.buildinfo' -delete
# Correct the permissions.
find %{buildroot} -name '*.so' -exec chmod 755 {} ';'


%check
%{__python2} setup.py test
pushd %{py3dir}
%{__python3} setup.py test
popd


%files
%doc README.rst TODO.txt
%license COPYING
%{python2_sitearch}/%{pkgname}-%{version}-py%{python2_version}.egg-info
%{python2_sitearch}/%{pkgname}
%{python2_sitearch}/_%{pkgname}.so
%{python2_sitearch}/%{pkgname}_cffi_*.so

%files -n python3-%{pkgname}
%doc README.rst TODO.txt
%license COPYING
%{python3_sitearch}/%{pkgname}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pkgname}
%{python3_sitearch}/_%{pkgname}.*.so
%{python3_sitearch}/%{pkgname}_cffi_*.so

%files doc
%doc docs/_build/html/*


%changelog
* Tue Jan 27 2015 Reiner Rottmann <reiner@rottmann.it> - 0.22.0-1
- Update to 0.22.0

* Mon Nov 17 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.4-1
- Update to 0.21.4

* Fri Sep 19 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.3-1
- Update to 0.21.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.2-2
- Add missing requirement
  https://bugzilla.redhat.com/show_bug.cgi?id=1129868

* Tue Aug 12 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.2-1
- Update to 0.21.2

* Tue Jul 29 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.1-1
- Update to 0.21.1

* Sun Jun 29 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.0-1
- Update to 0.21.0

* Sat Jun 21 2014 Christopher Meng <rpm@cicku.me> - 0.20.3-1
- Update to 0.20.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Mar 09 2014 Christopher Meng <rpm@cicku.me> - 0.20.2-1
- Update to 0.20.2

* Sun Dec 08 2013 Christopher Meng <rpm@cicku.me> - 0.20.0-1
- Update to 0.20.0
- Clarify the license

* Tue Oct 08 2013 Christopher Meng <rpm@cicku.me> - 0.19.1-2
- Split out -doc subpackage.
- Correct the libs permissions.

* Mon Oct 07 2013 Christopher Meng <rpm@cicku.me> - 0.19.1-1
- Update to 0.19.1

* Sat Aug 17 2013 Christopher Meng <rpm@cicku.me> - 0.19.0-4
- Add missing sphinx BR.

* Tue Aug 13 2013 Christopher Meng <rpm@cicku.me> - 0.19.0-3
- Remove unneeded files.

* Mon Aug 12 2013 Christopher Meng <rpm@cicku.me> - 0.19.0-2
- Add missing nose BR.
- Add docs.

* Thu Aug 01 2013 Christopher Meng <rpm@cicku.me> - 0.19.0-1
- Update to new release.

* Fri Apr 26 2013 Christopher Meng <rpm@cicku.me> - 0.18.1-1
- Update to new release.

* Mon Sep 24 2012 Christopher Meng <rpm@cicku.me> - 0.17.3-1
- Update to new release.

* Sun Jul 29 2012 Christopher Meng <rpm@cicku.me> - 0.17.2-1
- Update to new release.

* Fri Mar 30 2012 Christopher Meng <rpm@cicku.me> - 0.16.1-1
- Update to new release.

* Thu Mar 01 2012 Christopher Meng <rpm@cicku.me> - 0.16.0-1
- Initial Package.
