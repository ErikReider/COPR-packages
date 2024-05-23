Name:       autotiling
Version:    1.9.3
Release:    1%{?dist}
Summary:    Autotiling script for sway(fx)/i3
License:    GPLv3+
URL:        https://github.com/nwg-piotr/autotiling
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
Requires:       python
Requires:       python3-i3ipc
Requires:       bash

BuildArch:      noarch

%description
Script for sway and i3 to automatically switch the horizontal / vertical window split orientation

%prep
%autosetup -p1 -n autotiling-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l autotiling


%files -n autotiling -f %{pyproject_files}
%doc README.md
%{_bindir}/autotiling

%changelog
# let's skip this for now
