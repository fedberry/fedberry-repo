%define bname   fedberry
%define name    %{bname}-repo
%define version 25
%define release 2

Summary:    FedBerry Yum RPM Repositories
License:    GPLv3
Name:       %{name}
Version:    %{version}
Release:    %{release}%{?dist}
Group:      Development/Tools
URL:        https://github.com/fedberry
Source0:    RPM-GPG-KEY-fedberry-%{version}-primary
Source1:    %{bname}.repo
Source2:    %{bname}-testing.repo
Source3:    %{bname}-unstable.repo
Source4:    %{bname}-kernel-rt.repo
BuildArch:  noarch
Obsoletes:  raspberrypi-repo
Provides:   raspberrypi-repo
Conflicts:  raspberrypi-repo

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
install -m 644 RPM-GPG-KEY-fedberry-%{version}-primary $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-fedberry-%{version}-primary

%changelog
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
