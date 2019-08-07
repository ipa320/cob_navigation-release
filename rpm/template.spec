Name:           ros-melodic-cob-navigation-global
Version:        0.6.8
Release:        1%{?dist}
Summary:        ROS cob_navigation_global package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_navigation_global
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-amcl
Requires:       ros-melodic-cob-default-env-config
Requires:       ros-melodic-cob-linear-nav
Requires:       ros-melodic-cob-navigation-config
Requires:       ros-melodic-cob-scan-unifier
Requires:       ros-melodic-dwa-local-planner
Requires:       ros-melodic-map-server
Requires:       ros-melodic-move-base
Requires:       ros-melodic-rviz
Requires:       ros-melodic-topic-tools
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cob-default-env-config
BuildRequires:  ros-melodic-cob-supported-robots
BuildRequires:  ros-melodic-roslaunch

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
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Aug 07 2019 Felix Zeltner <fez@ipa.fraunhofer.de> - 0.6.8-1
- Autogenerated by Bloom

