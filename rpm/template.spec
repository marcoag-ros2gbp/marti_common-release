Name:           ros-melodic-swri-transform-util
Version:        2.7.1
Release:        0%{?dist}
Summary:        ROS swri_transform_util package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       geos-devel
Requires:       proj-devel
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-geographic-msgs
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-gps-common
Requires:       ros-melodic-nodelet
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-swri-math-util
Requires:       ros-melodic-swri-nodelet
Requires:       ros-melodic-swri-roscpp
Requires:       ros-melodic-swri-yaml-util
Requires:       ros-melodic-tf
Requires:       ros-melodic-topic-tools
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  geos-devel
BuildRequires:  pkgconfig
BuildRequires:  proj-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-geographic-msgs
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-gps-common
BuildRequires:  ros-melodic-nodelet
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-swri-math-util
BuildRequires:  ros-melodic-swri-nodelet
BuildRequires:  ros-melodic-swri-roscpp
BuildRequires:  ros-melodic-swri-yaml-util
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-topic-tools
BuildRequires:  yaml-cpp-devel

%description
The swri_transform_util package contains utility functions and classes for
transforming between coordinate frames.

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
* Fri Dec 14 2018 Marc Alban <malban@swri.org> - 2.7.1-0
- Autogenerated by Bloom

* Tue Dec 04 2018 Marc Alban <malban@swri.org> - 2.7.0-0
- Autogenerated by Bloom

* Sat Nov 03 2018 Marc Alban <malban@swri.org> - 2.6.0-0
- Autogenerated by Bloom

* Fri Oct 12 2018 Marc Alban <malban@swri.org> - 2.5.0-0
- Autogenerated by Bloom

* Tue Oct 09 2018 Marc Alban <malban@swri.org> - 2.4.0-0
- Autogenerated by Bloom

* Fri May 25 2018 Marc Alban <malban@swri.org> - 2.3.0-0
- Autogenerated by Bloom

* Fri May 11 2018 Marc Alban <malban@swri.org> - 2.2.1-0
- Autogenerated by Bloom

