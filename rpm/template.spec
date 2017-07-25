Name:           ros-kinetic-cob-navigation
Version:        0.6.5
Release:        0%{?dist}
Summary:        ROS cob_navigation package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_navigation
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-cob-linear-nav
Requires:       ros-kinetic-cob-map-accessibility-analysis
Requires:       ros-kinetic-cob-mapping-slam
Requires:       ros-kinetic-cob-navigation-config
Requires:       ros-kinetic-cob-navigation-global
Requires:       ros-kinetic-cob-navigation-local
Requires:       ros-kinetic-cob-navigation-slam
BuildRequires:  ros-kinetic-catkin

%description
The cob_navigation stack provides different navigation packages for Care-O-bot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Jul 25 2017 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.5-0
- Autogenerated by Bloom

