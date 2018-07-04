#
# spec file for package monitoring-plugins-check_notary
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           monitoring-plugins-notary
%define		base_name check_notary
Version:        0.0.1
Release:        0
Summary:        Check (docker) notary status plugin for Nagios
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-3.0-or-later 
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          System/Monitoring
Url:            https://github.com/M0ses/check_notary
Source:         check_notary-%{version}.tar.gz
BuildRequires:  nagios-rpm-macros
Requires:       perl(LWP::UserAgent)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Monitoring::Plugin)
Requires:       perl(JSON::MaybeXS)

%description
This plugin checks a (docker) notary status by fetching the changefeed.

%prep
%setup -q -n %{base_name}-%{version}

%build

%install
install -d -m755 %{buildroot}/%{nagios_plugindir}
install -m755 ./%{base_name} %{buildroot}/%{nagios_plugindir}/%{base_name}

%post
%postun

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/%{base_name}

%changelog
