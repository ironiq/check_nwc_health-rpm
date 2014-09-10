#
# spec file for package check_nwc_health
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%if ! 0%{?suse_version}
# Recreate OpenSUSE nagios-rpm-macros
%global nagios_plugindir %{_libdir}/nagios/plugins
%global nagios_user nagios
%global nagios_group nagios
%global nagios_plugindir %{_libdir}/nagios/plugins

%endif

Name:           check_nwc_health
Version:        3.0.3.7
Release:        0%{?dist}
License:        GPL-2.0+
Summary:        Checks the hardware health of network components
Url:            http://labs.consol.de/lang/de/nagios/check_nwc_health/
Group:          System/Monitoring
Source:         %{name}-%{version}.tar.gz
Requires:       perl(AutoLoader)
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::MD5)
Requires:       perl(Errno)
Requires:       perl(File::Basename)
Requires:       perl(File::Path)
Requires:       perl(Getopt::Long)
Requires:       perl(IO::File)
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  nagios-rpm-macros 
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif

%description
This plugin checks the hardware health and various interface metrics
of network components like switches and routers.

The (incomplete) list includes:
Cisco IOS, Cisco Nexus, F5 BIG-IP, CheckPoint Firewall1, Juniper NetScreen, HP
Procurve, Nortel, Brocade 4100/4900, EMC DS 4700, EMC DS 24, Allied Telesyn.
Blue Coat SG600, Cisco Wireless Lan Controller 5500, Brocade ICX6610-24-HPOE,
NX-OS, FOUNDRY-SN-AGENT-MIB, FRITZ!BOX 7390, FRITZ!DECT 200, Juniper IVE,
Pulse-Gateway MAG4610, Cisco IronPort AsyncOS, Foundry…

%prep
%setup -q

%build
%configure \
    --prefix=%{nagios_plugindir} \
	--with-nagios-user=%{nagios_user} \
	--with-nagios-group=%{nagios_group} \
	--with-perl=%{_bindir}/perl \
	--with-degrees='celsius' \
	--enable-perfdata \
	--enable-extendedinfo
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{nagios_plugindir}
mv  %{buildroot}%{_libexecdir}/check_nwc_health %{buildroot}%{nagios_plugindir}/

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING THANKS TODO

# RedHat doesn't allow multiple ownership of directories
%if 0%{?suse_version}
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%endif
%{nagios_plugindir}/check_nwc_health

%changelog
* Wed Sep 10 2014 John Morris <john@zultron.com> - 3.0.3.7-0
- Update to 3.0.3.7
- Port to Red Hat

* Sat Jul 26 2014 lars@linux-schulserver.de
- initial version 3.0i
