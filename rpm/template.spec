Name:           ros-indigo-cob-navigation-global
Version:        0.6.0
Release:        2%{?dist}
Summary:        ROS cob_navigation_global package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_navigation_global
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-amcl
Requires:       ros-indigo-cob-default-env-config
Requires:       ros-indigo-cob-linear-nav
Requires:       ros-indigo-cob-navigation-config
Requires:       ros-indigo-cob-scan-unifier
Requires:       ros-indigo-map-server
Requires:       ros-indigo-move-base
Requires:       ros-indigo-navigation
Requires:       ros-indigo-rviz
Requires:       ros-indigo-topic-tools
BuildRequires:  ros-indigo-catkin

%description
This package holds config and launch files for running the move_base node on the
Care-O-bot. The move_base node is configured to run over a pre-specified static
map.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 10 2014 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.0-2
- Autogenerated by Bloom

* Wed Sep 10 2014 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.0-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.0-1
- Autogenerated by Bloom

