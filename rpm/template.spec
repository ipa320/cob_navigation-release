Name:           ros-indigo-cob-map-accessibility-analysis
Version:        0.6.6
Release:        0%{?dist}
Summary:        ROS cob_map_accessibility_analysis package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_map_accessibility_analysis
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       opencv-devel
Requires:       pcl-devel
Requires:       ros-indigo-cob-3d-mapping-msgs
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
BuildRequires:  boost-devel
BuildRequires:  opencv-devel
BuildRequires:  pcl-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-3d-mapping-msgs
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf

%description
cob_map_accessibility_analysis receives the map from navigation as well as
obstacles and inflates_obstacles topics to assemble a common obstacle map. Upon
request, this node checks the accessibility of poses within thin map by (i)
checking whether the pose itself is free and by (ii) checking whether there is a
closed path from robot to the goal pose.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Jan 07 2018 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.6-0
- Autogenerated by Bloom

* Tue Jul 18 2017 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.5-0
- Autogenerated by Bloom

