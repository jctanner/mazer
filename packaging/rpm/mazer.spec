%define name mazer
%define release_date %(date "+%a %b %e %Y")

%if 0%{?rhel} == 5
%define __python2 /usr/bin/python26
%endif

Name:      %{name}
Version:   %{rpmversion}
Release:   %{rpmrelease}%{?dist}%{?repotag}
Url:       https://www.ansible.com
Summary:   SSH-based application deployment, configuration management, and IT orchestration platform
License:   GPLv3+
Group:     Development/Libraries
Source:    https://releases.ansible.com/ansible/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%{!?__python2: %global __python2 /usr/bin/python2.6}
%{!?python_sitelib: %global python_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

BuildArch: noarch

Requires: sshpass

%description

Ansible is a radically simple model-driven configuration management,
multi-node deployment, and orchestration engine. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%prep
%setup -q -n %{name}-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/mazer*
%{python_sitelib}/ansible_galaxy/*
%{python_sitelib}/ansible_galaxy_cli/*
%{_bindir}/mazer*

%changelog

* %{release_date} Ansible, Inc. <info@ansible.com> - %{rpmversion}-%{rpmrelease}
- Release %{rpmversion}-%{rpmrelease}
