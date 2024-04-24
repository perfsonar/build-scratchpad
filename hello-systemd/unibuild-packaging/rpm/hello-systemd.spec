#
# RPM Spec for Unibuild Hello-Systemd
#

Name:		hello-systemd
Version:	1.0
Release:	1%{?dist}

Summary:	Systemd Test

BuildArch:	noarch
License:	Apache 2.0
Group:		Utilities/Text
Vendor:		The perfSONAR Development Team <perfsonar-developer@internet2.edu>
#URL:		https://...

#Source0:	No sources

Provides:	%{name} = %{version}-%{release}


%description
Test package that does things with systemd

%build
true

%post

ps -ef

systemctl status

%files
# No files.
