%define debug_package %{nil}

%global github_version  0.56.0
%global rpm_version     0.56.0

Name:           hugo
Version:        %{rpm_version}
Release:        1%{?dist}
Summary:        A Fast and Flexible Static Site Generator
Group:          Applications/System
License:        Apache 2.0
URL:            https://github.com/gohugoio/hugo
BuildRequires:  git golang

%description
Hugo is a static HTML and CSS website generator written in Go. It is optimized for speed, easy use and configurability. Hugo takes a directory with content and templates and renders them into a full HTML website.

%prep
wget https://github.com/gohugoio/hugo/archive/v%{github_version}.tar.gz
tar xzf v%{github_version}.tar.gz
mkdir -p %{_builddir}/src/github.com/gohugoio/
cd %{_builddir}/src/github.com/gohugoio/
mv %{_builddir}/%{name}-%{github_version} %{name}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/gohugoio/hugo
GO111MODULE=on go install

%install
mkdir -p %{buildroot}%{_bindir}

cp %{_builddir}/bin/hugo %{buildroot}%{_bindir}


%files
%{_bindir}/hugo

%changelog
* Fri Jul 26 2019 Jamie Curnow <jc@jc21.com> 0.56.0-1
- New release 0.56.0

* Mon May 20 2019 Jamie Curnow <jc@jc21.com> 0.55.6-1
- New release 0.55.6

* Fri May 3 2019 Jamie Curnow <jc@jc21.com> 0.55.5-1
- New release 0.55.5

* Fri Apr 26 2019 Jamie Curnow <jc@jc21.com> 0.55.4-1
- New release 0.55.4

* Tue Apr 23 2019 Jamie Curnow <jc@jc21.com> 0.55.3-1
- New release 0.55.3

* Thu Apr 18 2019 Jamie Curnow <jc@jc21.com> 0.55.2-1
- New release 0.55.2

* Tue Apr 9 2019 Jamie Curnow <jc@jc21.com> 0.55.0-1
- New release 0.55.0

* Wed Feb 6 2019 Jamie Curnow <jc@jc21.com> 0.54.0-1
- New release 0.54.0

* Thu Jan 3 2019 Jamie Curnow <jc@jc21.com> 0.53.0-1
- New release 0.53

* Thu Nov 8 2018 Jamie Curnow <jc@jc21.com> 0.51.0-1
- New release 0.51

* Tue Oct 30 2018 Jamie Curnow <jc@jc21.com> 0.50.0-1
- New release 0.50

* Fri Oct 12 2018 Jamie Curnow <jc@jc21.com> 0.49.2-1
- New release 0.49.2

* Tue Sep 25 2018 Jamie Curnow <jc@jc21.com> 0.49.0-1
- New release 0.49.0

* Fri Sep 21 2018 Jamie Curnow <jc@jc21.com> 0.48.0-1
- New release 0.48.0

* Wed Aug 29 2018 Jamie Curnow <jc@jc21.com> 0.47.1-1
- New release 0.47.1

* Wed Jun 6 2018 Jamie Curnow <jc@jc21.com> 0.41-1
- New release 0.41

