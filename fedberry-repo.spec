%define bname   fedberry
%define name    %{bname}-repo
%define versions 24 25 26 27 28 29

Summary:    FedBerry Yum RPM Repositories
License:    GPLv3
Name:       %{name}
Version:    29
Release:    1%{?dist}
Group:      Development/Tools
URL:        https://github.com/%{name}
Source1:    %{url}/raw/master/%{bname}.repo
Source2:    %{url}/raw/master/%{bname}-testing.repo
Source3:    %{url}/raw/master/%{bname}-unstable.repo
Source4:    %{url}/raw/master/%{bname}-kernel-rt.repo
Source5:    %{url}/raw/master/fedora.repo
Source6:    %{url}/raw/master/fedora-updates.repo
Source7:    %{url}/raw/master/fedora-updates-testing.repo
Source8:    %{url}/raw/master/fedora-cisco-openh264.repo
Source9:    %{url}/raw/master/RPM-GPG-KEY-%{bname}-24-primary
Source10:   %{url}/raw/master/RPM-GPG-KEY-%{bname}-25-primary
Source11:   %{url}/raw/master/RPM-GPG-KEY-%{bname}-26-primary
Source12:   %{url}/raw/master/RPM-GPG-KEY-%{bname}-27-primary
Source13:   %{url}/raw/master/RPM-GPG-KEY-%{bname}-28-primary
Source14:   %{url}/raw/master/RPM-GPG-KEY-%{bname}-29-primary
Requires:   fedora-gpg-keys
BuildArch:  noarch

Provides:   fedora-repos
Obsoletes:  fedora-repos
Conflicts:  fedora-repos

%description
Package containing Fedberry Yum RPM Repository configuration files and GPG keys.


%prep
%setup -c -T
cp -a %{sources} .


%build


%install
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
install -m 644 *.repo %{buildroot}%{_sysconfdir}/yum.repos.d/

mkdir -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg
for i in %{versions}; do
    install -m 644 RPM-GPG-KEY-%{bname}-$i-primary %{buildroot}%{_sysconfdir}/pki/rpm-gpg/
done


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-%{bname}-*-primary


%changelog
* Tue Oct 09 2018 Vaughan <vaughan at agrez dot net> 29-1
- FedBerry 29 release

* Tue Oct 09 2018 Vaughan <vaughan at agrez dot net> 28-9
- Add FedBerry 29 release key

* Sat Jul 28 2018 Vaughan <vaughan at agrez dot net> 28-8
- Add kernel-headers to fedora repo excludes

* Tue Jul 24 2018 Vaughan <vaughan at agrez dot net> 28-7
- Add plymouth-plugin-two-step to fedora repo excludes

* Thu Jul 19 2018 Vaughan <vaughan at agrez dot net> 28-6
- Remove wildcards from repo excludes
  (PackageKit does not support/honour them)

* Mon Jul 16 2018 Vaughan <vaughan at agrez dot net> 28-5
- Fix F28 'update' repo urls

* Thu Jul 12 2018 Vaughan <vaughan at agrez dot net> 28-4
- Fix fedora repo excludes

* Sun Jul 08 2018 Vaughan <vaughan at agrez dot net> 28-3
- Update excludes
- Misc spec adjusments

* Tue Jun 26 2018 Vaughan <vaughan at agrez dot net> 28-2
- Fix Source urls
- Update spec description

* Tue Jun 26 2018 Vaughan <vaughan at agrez dot net> 28-1
- Update for FedBerry 28 release
- Add FedBerry 28 release key

* Wed Mar 21 2018 Vaughan <vaughan at agrez dot net> 27-3
- Requires fedora-gpg-keys

* Sun Mar 11 2018 Vaughan <vaughan at agrez dot net> 27-2
- Add fedora repo files
- Update fedberry repo files

* Thu Nov 23 2017 Vaughan <vaughan at agrez dot net> 27-1
- Update for FedBerry 27 release
- Add FedBerry 27 release key

* Sat Jul 08 2017 Vaughan <vaughan at agrez dot net> 26-1
- Update for FedBerry 26 release
- Add FedBerry 26 primary release key

* Fri Jun 23 2017 Vaughan <vaughan at agrez dot net> 25-6
- Add a workaround for dnf 'system-upgrade plugin' issues

* Wed Apr 12 2017 Vaughan <vaughan at agrez dot net> 25-5
- Set mirrorlist to expire every 24 hours

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
