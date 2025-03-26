Name:      azote
Version:   1.14.2
Release:   1
BuildArch: noarch
Summary:   Wallpaper and color manager for Sway, i3 and some other WMs
Group:     WM/NWG
# GPLv3: main program
# BSD: colorthief.py
License:   GPL-3.0-only and BSD-1-Clause
URL:       https://github.com/nwg-piotr/azote
Source0:   https://github.com/nwg-piotr/azote/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: python
BuildRequires: python-setuptools
BuildRequires: pkgconfig(python)

Requires: python-pillow
Requires: python-gobject3
Requires: python-gi
Requires: ((feh and xrandr) if x11-server)
Requires: ((swaybg and wlr-randr) if wayfire)
Requires: python-cairo

Recommends: python-send2trash
Recommends: imagemagick
Recommends: ((maim and slop) if x11-server)

Provides: bundled(python3-colorthief) = 0.2.1

%description
Azote is a GTK+3 - based picture browser and background setter, as the
front-end to the swaybg (sway/Wayland) and feh (X windows) commands. It
also includes several color management tools.

The program is confirmed to work on sway, i3, Openbox, Fluxbox and dwm
window managers, on Arch Linux, Void Linux, Debian and Fedora.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install
install -D -m 0644 dist/azote.svg %{buildroot}%{_datadir}/azote/azote.svg
install -D -m 0644 dist/azote.desktop %{buildroot}%{_datadir}/applications/azote.desktop

%files
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-*.egg-info/
%{_bindir}/%{name}
%{_datadir}/azote/azote.svg
%{_datadir}/applications/azote.desktop
%doc README.md
%license LICENSE LICENSE-COLORTHIEF
