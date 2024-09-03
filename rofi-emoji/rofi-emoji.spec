Name:    rofi-emoji
Version: 4.0.0
Release: 1%{?dist}
Summary: Emoji selector plugin for Rofi 

License: MIT
URL:     https://github.com/Mange/rofi-emoji
Source:  %{URL}/archive/v%{version}/rofi-emoji-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: meson
BuildRequires: rofi-wayland
# pkgbuild(rofi) uses system repo, not my package for some reason
BuildRequires: rofi-wayland-devel

requires:      wl-clipboard

Provides:      rofi-emoji = %{version}
Conflicts:     rofi-emoji

%description
An emoji selector plugin for Rofi that copies the selected emoji to the
clipboard, among other things.

%prep
%autosetup -p1 -n rofi-emoji-%{version}


%build
autoreconf -i
%configure
make


%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_datadir}/rofi-emoji/LICENSE
rm -rf %{buildroot}%{_datadir}/rofi-emoji/README.md

%check
make check


%files
%doc README.md
%license LICENSE
%{_libdir}/rofi/emoji.so
%{_datadir}/rofi-emoji/all_emojis.txt
%{_datadir}/rofi-emoji/clipboard-adapter.sh

%changelog
# let's skip this for now
