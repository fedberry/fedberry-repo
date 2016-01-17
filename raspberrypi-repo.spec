%define name    raspberrypi-repo
%define version   0.3
%define release   1

Summary:    Raspberry Pi 2 Yum RPM Repository
License:    GPLv3
Name:       %{name}
Version:    %{version}
Release:    %{release}%{?dist}
Group:      Development/Tools
Source:     %{name}-%{version}.tar.xz
BuildArch:  noarch

%description
Package containing a Yun RPM Repository configuration files and GPG key.
 
%prep
%setup -q
 
%build
 
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
install -m 644 rpi2-rpm.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
install -m 644 RPM-GPG-KEY-rpi2 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
 
%clean
rm -rf $RPM_BUILD_ROOT
 
%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpi2-rpm.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpi2
 
%changelog
* Wed Oct 07 2015 Vaughan <vaughan at agrez dot net> 0.3-1
- Update for F23 repo

* Fri Sep 25 2015 Vaughan <vaughan at agrez dot net> 0.2-1
- Add metadata_expire=6h to repo config

* Tue Sep 08 2015 Vaughan <vaughan at agrez dot net> 0.1-1
- Initial release. 
