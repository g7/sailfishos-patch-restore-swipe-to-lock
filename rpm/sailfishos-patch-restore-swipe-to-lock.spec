# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-patch-restore-swipe-to-lock

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Restore swipe to lock
Version:    2.0.2.43
Release:    1
Group:      Applications/Productivity
License:    GPLv2+
BuildArch:  noarch
URL:        http://me.medesimo.eu
Source0:    %{name}-%{version}.tar.bz2
Source100:  sailfishos-patch-restore-swipe-to-lock.yaml
Requires:   patchmanager
Requires:   jolla-settings-system >= 0.6.8.1-10.78.1.jolla
Requires:   lipstick-jolla-home-qt5 >= 0.33.36.1-10.112.7.jolla
Requires:   sailfish-version >= 2.0.2-10.35.43.jolla

%description
Patch that restores the swipe to lock functionality.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%preun
# >> preun
if [ -x /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u eugenio-restore-swipe-to-lock || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager
# >> files
# << files
