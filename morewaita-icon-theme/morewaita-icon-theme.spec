Name:       morewaita-icon-theme
Version:    49
Release:    1%{?dist}
Summary:    An expanded Adwaita-styled companion icon theme with extra icons
License:    GPL-3.0-or-later
URL:        https://github.com/somepaulo/MoreWaita
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

Requires:       adwaita-icon-theme

BuildArch:      noarch

%description
An expanded Adwaita-styled companion icon theme, built largely upon the work of GNOME's Adwaita designers and GNOME Circle apps' developers, as well as inspiration from the Papirus icon theme designers, and a touch of tinkering from myself and a few others.

%prep
%autosetup -p1 -n MoreWaita-%{version}

%build
rm -rf _dev/

%install
install -d %{buildroot}%{_datadir}/icons/MoreWaita
cp -r * %{buildroot}%{_datadir}/icons/MoreWaita

%files
%doc README.md
%{_datadir}/icons/MoreWaita/

%changelog
# let's skip this for now
