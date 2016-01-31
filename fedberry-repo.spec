%define bname   fedberry
%define name    %{bname}-repo
%define version 23
%define release 0.1

Summary:    FedBerry Yum RPM Repositories
License:    GPLv3
Name:       %{name}
Version:    %{version}
Release:    %{release}%{?dist}
Group:      Development/Tools
Source0:    RPM-GPG-KEY-rpi2
Source1:    %{bname}.repo
Source2:    %{bname}-testing.repo
Source3:    %{bname}-unstable.repo
BuildArch:  noarch
Obsoletes:  raspberrypi-repo
Provides:   raspberrypi-repo
Conflicts:  raspberrypi-repo

%description
Package containing a Yum RPM Repository configuration files and GPG key.

%prep
%setup -c -T
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
install -m 644 *.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
install -m 644 RPM-GPG-KEY-rpi2 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpi2

%changelog
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
