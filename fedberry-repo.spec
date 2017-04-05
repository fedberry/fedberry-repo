%define bname   fedberry
%define name    %{bname}-repo
%define versions 24 25

Summary:    FedBerry Yum RPM Repositories
License:    GPLv3
Name:       %{name}
Version:    25
Release:    4%{?dist}
Group:      Development/Tools
URL:        https://github.com/%{bname}
Source1:    %{bname}.repo
Source2:    %{bname}-testing.repo
Source3:    %{bname}-unstable.repo
Source4:    %{bname}-kernel-rt.repo
Source5:    RPM-GPG-KEY-%{bname}-24-primary
Source6:    RPM-GPG-KEY-%{bname}-25-primary
BuildArch:  noarch


%description
Package containing a Yum RPM Repository configuration files and GPG key.

%prep
%setup -c -T
cp -a %{sources} .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
install -m 644 *.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
for i in %{versions}; do
    install -m 644 RPM-GPG-KEY-%{bname}-$i-primary $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-%{bname}-*-primary

%changelog
* Wed Apr 05 2017 Vaughan <vaughan at agrez dot net> 25-4
- Switch to using mirrorlists in repo files

* Tue Mar 07 2017 Vaughan <vaughan at agrez dot net> 25-3
- Add previous FedBerry 24 primary release key

* Sun Feb 26 2017 Vaughan <vaughan at agrez dot net> 25-2
- Add kernel-rt repo

* Mon Jan 02 2017 Vaughan <vaughan at agrez dot net> 25-1
- Update for FedBerry 25 release

* Sat Aug 20 2016 Vaughan <vaughan at agrez dot net> 24-0.2
- List all urls in one 'baseurl' (fillarios)

* Wed Jun 15 2016 Vaughan <vaughan at agrez dot net> 24-0.1
- Update for FedBerry 24 release
- Add new FedBerry 24 release key
- Update repo files for altered repository structure

* Sat Feb 06 2016 Vaughan <vaughan at agrez dot net> 23-0.3
- Repos are moving, replace all existing repo files

* Thu Feb 04 2016 Vaughan <vaughan at agrez dot net> 23-0.2
- Update to reflect new repo structure
- Add our new fedberry.org repo (fedorapeople is now a mirror)

* Sun Jan 31 2016 Vaughan <vaughan at agrez dot net> 23-0.1
- Rename package to fedberry-repo
- Version now follows FedBerry distro release version
- Split out files from tar.xz
- Add fedberry-unstable repo

* Tue Jan 19 2016 Vaughan <vaughan at agrez dot net> 0.4-1
- Rename repo file to 'fedberry'
- Add fedberry-testing repo

* Wed Oct 07 2015 Vaughan <vaughan at agrez dot net> 0.3-1
- Update for F23 repo

* Fri Sep 25 2015 Vaughan <vaughan at agrez dot net> 0.2-1
- Add metadata_expire=6h to repo config

* Tue Sep 08 2015 Vaughan <vaughan at agrez dot net> 0.1-1
- Initial release. 
