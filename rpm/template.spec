Name:           ros-indigo-cob-linear-nav
Version:        0.6.3
Release:        0%{?dist}
Summary:        ROS cob_linear_nav package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_linear_nav
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-move-base-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-move-base-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf

%description
cob_linear_nav provides a simple navigation instrument driving on a linear path
from current position to goal without any planning or obstacle avoidance
capabilites. Obstacle avoidance should be carried out in other package, e.g.
cob_collision_velocity_filter.

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
* Mon Aug 31 2015 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.3-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.2-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.1-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.0-2
- Autogenerated by Bloom

* Wed Sep 10 2014 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.0-1
- Autogenerated by Bloom

* Wed Sep 10 2014 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.0-0
- Autogenerated by Bloom

