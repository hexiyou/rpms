# $Id$
# Authority: dag

Summary: Tool to manage WBFS files and WBFS partitions
Name: wbfs_file
Version: 2.9
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://cfg-loader.googlecode.com/

Source: http://cfg-loader.googlecode.com/files/wbfs_file_%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: i386

%description
wbfs_file is a tool to manage WBFS files and WBFS partitions.

%prep
%setup -n %{name}_%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 linux/wbfs_file %{buildroot}%{_bindir}/wbfs_file

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc readme.txt readme_orig.txt scripts/
%{_bindir}/wbfs_file

%changelog
* Tue Jan 19 2010 Dag Wieers <dag@wieers.com> - 2.9-1
- Updated to release 2.9.

* Sun Jan 17 2010 Dag Wieers <dag@wieers.com> - 2.8-1
- Updated to release 2.8.

* Fri Jan 01 2010 Dag Wieers <dag@wieers.com> - 2.2-1
- Initial package. (using DAR)
