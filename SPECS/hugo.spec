%define debug_package %{nil}

Name:           hugo
Version:        0.110.0
Release:        1
Summary:        A Fast and Flexible Static Site Generator
Group:          Applications/System
License:        Apache 2.0
URL:            https://github.com/gohugoio/hugo
Source:         https://github.com/gohugoio/hugo/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Hugo is a static HTML and CSS website generator written in Go. It is optimized for speed, easy use and configurability. Hugo takes a directory with content and templates and renders them into a full HTML website.

%prep
%setup -qn %{name}-%{version}

%build
go build -o %{_builddir}/bin/%{name} main.go

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc LICENSE *.md docs/*.md

%changelog
* Fri Feb 3 2023 Jamie Curnow <jc@jc21.com> 0.110.0-1
- New release 0.110.0

* Tue Jan 3 2023 Jamie Curnow <jc@jc21.com> 0.109.0-1
- New release 0.109.0

* Mon Sep 26 2022 Jamie Curnow <jc@jc21.com> 0.104.0-1
- New release 0.104.0

* Tue Sep 20 2022 Jamie Curnow <jc@jc21.com> 0.103.1-1
- New release 0.103.1

* Mon Mar 28 2022 Jamie Curnow <jc@jc21.com> 0.96.0-1
- New release 0.96.0

* Thu Mar 17 2022 Jamie Curnow <jc@jc21.com> 0.95.0-1
- New release 0.95.0

* Tue Mar 12 2022 Jamie Curnow <jc@jc21.com> 0.94.2-1
- New release 0.94.2

* Fri Mar 11 2022 Jamie Curnow <jc@jc21.com> 0.94.0-1
- New release 0.94.0

* Mon Jan 31 2022 Jamie Curnow <jc@jc21.com> 0.92.1-1
- New release 0.92.1

* Fri Dec 10 2021 Jamie Curnow <jc@jc21.com> 0.90.0-1
- New release 0.90.0

* Wed Nov 3 2021 Jamie Curnow <jc@jc21.com> 0.89.0-1
- New release 0.89.0

* Mon Sep 6 2021 Jamie Curnow <jc@jc21.com> 0.88.1-1
- New release 0.88.1

* Wed Aug 4 2021 Jamie Curnow <jc@jc21.com> 0.87.0-1
- New release 0.87.0

* Thu Jul 22 2021 Jamie Curnow <jc@jc21.com> 0.86.0-1
- New release 0.86.0

* Tue Jul 06 2021 Jamie Curnow <jc@jc21.com> 0.85.0-1
- New release 0.85.0

* Mon Jul 05 2021 Jamie Curnow <jc@jc21.com> 0.84.4-1
- New release 0.84.4

* Wed Jun 30 2021 Jamie Curnow <jc@jc21.com> 0.84.3-1
- New release 0.84.3

* Tue Jun 29 2021 Jamie Curnow <jc@jc21.com> 0.84.2-1
- New release 0.84.2

* Fri Jun 25 2021 Jamie Curnow <jc@jc21.com> 0.84.1-1
- New release 0.84.1

* Tue May 4 2021 Jamie Curnow <jc@jc21.com> 0.83.1-1
- New release 0.83.1

* Wed Apr 21 2021 Jamie Curnow <jc@jc21.com> 0.82.1-1
- New release 0.82.1

* Mon Mar 22 2021 Jamie Curnow <jc@jc21.com> 0.82.0-1
- New release 0.82.0

* Mon Feb 22 2021 Jamie Curnow <jc@jc21.com> 0.81.0-1
- New release 0.81.0

* Mon Jan 4 2021 Jamie Curnow <jc@jc21.com> 0.80.0-1
- New release 0.80.0

* Mon Dec 21 2020 Jamie Curnow <jc@jc21.com> 0.79.1-1
- New release 0.79.1

* Sun Nov 29 2020 Jamie Curnow <jc@jc21.com> 0.79.0-1
- New release 0.79.0

* Mon Nov 16 2020 Jamie Curnow <jc@jc21.com> 0.78.2-1
- New release 0.78.2

* Fri Nov 6 2020 Jamie Curnow <jc@jc21.com> 0.78.1-1
- New release 0.78.1

* Wed Nov 4 2020 Jamie Curnow <jc@jc21.com> 0.78.0-1
- New release 0.78.0

* Mon Nov 2 2020 Jamie Curnow <jc@jc21.com> 0.77.0-1
- New release 0.77.0

* Thu Oct 15 2020 Jamie Curnow <jc@jc21.com> 0.76.5-1
- New release 0.76.5

* Tue Oct 13 2020 Jamie Curnow <jc@jc21.com> 0.76.4-1
- New release 0.76.4

* Fri Oct 9 2020 Jamie Curnow <jc@jc21.com> 0.76.3-1
- New release 0.76.3

* Fri Sep 18 2020 Jamie Curnow <jc@jc21.com> 0.75.1-1
- New release 0.75.1

* Fri Jul 24 2020 Jamie Curnow <jc@jc21.com> 0.74.3-1
- New release 0.74.3

* Tue Jul 14 2020 Jamie Curnow <jc@jc21.com> 0.74.1-1
- New release 0.74.1

* Wed Jun 24 2020 Jamie Curnow <jc@jc21.com> 0.73.0-1
- New release 0.73.0

* Mon Jun 1 2020 Jamie Curnow <jc@jc21.com> 0.72.0-1
- New release 0.72.0

* Tue May 26 2020 Jamie Curnow <jc@jc21.com> 0.71.1-1
- New release 0.71.1

* Tue May 19 2020 Jamie Curnow <jc@jc21.com> 0.71.0-1
- New release 0.71.0

* Thu May 7 2020 Jamie Curnow <jc@jc21.com> 0.70.0-1
- New release 0.70.0

* Mon Apr 27 2020 Jamie Curnow <jc@jc21.com> 0.69.2-1
- New release 0.69.2

* Thu Apr 23 2020 Jamie Curnow <jc@jc21.com> 0.69.1-1
- New release 0.69.1

* Tue Apr 14 2020 Jamie Curnow <jc@jc21.com> 0.69.0-1
- New release 0.69.0

* Wed Mar 25 2020 Jamie Curnow <jc@jc21.com> 0.68.3-1
- New release 0.68.3

* Tue Mar 24 2020 Jamie Curnow <jc@jc21.com> 0.68.1-1
- New release 0.68.1

* Mon Mar 16 2020 Jamie Curnow <jc@jc21.com> 0.67.1-1
- New release 0.67.1

* Tue Mar 10 2020 Jamie Curnow <jc@jc21.com> 0.67.0-1
- New release 0.67.0

* Wed Mar 4 2020 Jamie Curnow <jc@jc21.com> 0.66.0-1
- New release 0.66.0

* Mon Feb 24 2020 Jamie Curnow <jc@jc21.com> 0.65.3-1
- New release 0.65.3

* Fri Feb 21 2020 Jamie Curnow <jc@jc21.com> 0.65.1-1
- New release 0.65.1

* Mon Feb 10 2020 Jamie Curnow <jc@jc21.com> 0.64.1-1
- New release 0.64.1

* Wed Feb 5 2020 Jamie Curnow <jc@jc21.com> 0.64.0-1
- New release 0.64.0

* Tue Jan 28 2020 Jamie Curnow <jc@jc21.com> 0.63.2-1
- New release 0.63.2

* Fri Jan 24 2020 Jamie Curnow <jc@jc21.com> 0.63.1-1
- New release 0.63.1

* Mon Jan 6 2020 Jamie Curnow <jc@jc21.com> 0.62.2-1
- New release 0.62.2

* Thu Jan 2 2020 Jamie Curnow <jc@jc21.com> 0.62.1-1
- New release 0.62.1

* Thu Dec 26 2019 Jamie Curnow <jc@jc21.com> 0.62.0-1
- New release 0.62.0

* Thu Dec 12 2019 Jamie Curnow <jc@jc21.com> 0.61.0-1
- New release 0.61.0

* Tue Dec 3 2019 Jamie Curnow <jc@jc21.com> 0.60.1-1
- New release 0.60.1

* Fri Nov 1 2019 Jamie Curnow <jc@jc21.com> 0.59.1-1
- New release 0.59.1

* Tue Oct 22 2019 Jamie Curnow <jc@jc21.com> 0.59.0-1
- New release 0.59.0

* Fri Sep 20 2019 Jamie Curnow <jc@jc21.com> 0.58.3-1
- New release 0.58.3

* Mon Sep 16 2019 Jamie Curnow <jc@jc21.com> 0.58.2-1
- New release 0.58.2

* Mon Sep 9 2019 Jamie Curnow <jc@jc21.com> 0.58.1-1
- New release 0.58.1

* Thu Sep 5 2019 Jamie Curnow <jc@jc21.com> 0.58.0-1
- New release 0.58.0

* Mon Aug 19 2019 Jamie Curnow <jc@jc21.com> 0.57.2-1
- New release 0.57.2

* Fri Aug 16 2019 Jamie Curnow <jc@jc21.com> 0.57.1-1
- New release 0.57.1

* Thu Aug 15 2019 Jamie Curnow <jc@jc21.com> 0.57.0-1
- New release 0.57.0

* Thu Aug 1 2019 Jamie Curnow <jc@jc21.com> 0.56.3-1
- New release 0.56.3

* Wed Jul 31 2019 Jamie Curnow <jc@jc21.com> 0.56.2-1
- New release 0.56.2

* Mon Jul 29 2019 Jamie Curnow <jc@jc21.com> 0.56.1-1
- New release 0.56.1

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

