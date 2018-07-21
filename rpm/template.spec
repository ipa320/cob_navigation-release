Name:           ros-indigo-cob-mapping-slam
Version:        0.6.7
Release:        0%{?dist}
Summary:        ROS cob_mapping_slam package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_mapping_slam
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-navigation-global
Requires:       ros-indigo-gmapping
BuildRequires:  ros-indigo-catkin

%description
cob_mapping_slam holds launch files for running SLAM using the gmapping package.

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
* Sat Jul 21 2018 Felix Zeltner <fez@ipa.fraunhofer.de> - 0.6.7-0
- Autogenerated by Bloom

* Sun Jan 07 2018 Felix Zeltner <fez@ipa.fraunhofer.de> - 0.6.6-0
- Autogenerated by Bloom

* Tue Jul 18 2017 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.5-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.4-0
- Autogenerated by Bloom

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

