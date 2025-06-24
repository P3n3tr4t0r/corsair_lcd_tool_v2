Name:           corsair_lcd_tool_v2
Version:        1.0.0
Release:        1%{?dist}
Summary:        Tool for managing Corsair LCDs via Python

License:        MIT
URL:            https://github.com/shutdown4life/corsair_lcd_tool_v2
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3
Requires:       python3-numpy
Requires:       python3-opencv
Requires:       python3-PyQt6
Requires:       python3-PyYAML
Requires:       python3-pyusb

%description
A Python-based tool to manage Corsair LCD screens. This package includes an installer script and a setup script that runs automatically upon installation.

%prep
%setup -q

%build
# No build step is required for plain Python and shell scripts

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/%{name}
cp -a install.sh corsair_lcd_tool.py %{buildroot}/usr/share/%{name}/
chmod +x %{buildroot}/usr/share/%{name}/install.sh
chmod +x %{buildroot}/usr/share/%{name}/corsair_lcd_tool.py
cp corsair-lcd-tool.png %{buildroot}/usr/share/%{name}/corsair-lcd-tool.png

mkdir -p %{buildroot}/usr/share/applications
cp corsair_lcd_tool.desktop %{buildroot}/usr/share/applications/

mkdir -p %{buildroot}/usr/bin
ln -sr %{buildroot}/usr/share/%{name}/install.sh %{buildroot}/usr/bin/%{name}-install
ln -sr %{buildroot}/usr/share/%{name}/corsair_lcd_tool.py %{buildroot}/usr/bin/corsair-lcd-tool

mkdir -p %{buildroot}/usr/share/icons/hicolor/48x48/apps
cp corsair-lcd-tool.png %{buildroot}/usr/share/icons/hicolor/48x48/apps/corsair-lcd-tool.png

%files
%license LICENSE
%doc README.md
/usr/share/%{name}/install.sh
/usr/share/%{name}/corsair_lcd_tool.py
/usr/share/%{name}/corsair-lcd-tool.png
/usr/bin/%{name}-install
/usr/bin/corsair-lcd-tool
/usr/share/applications/corsair_lcd_tool.desktop
/usr/share/icons/hicolor/48x48/apps/corsair-lcd-tool.png

%post
echo "Running install.sh to set up udev rules..." > /tmp/corsair_lcd_tool_post.log
/bin/bash /usr/share/%{name}/install.sh >> /tmp/corsair_lcd_tool_post.log 2>&1 || echo "install.sh failed" >> /tmp/corsair_lcd_tool_post.log

%changelog
* Thu Jun 19 2025 ShUtDoWn discord @shutdown4life - 1.0.0-1
- Initial RPM release with automatic post-install script