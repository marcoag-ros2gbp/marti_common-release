Name:           ros-lunar-swri-route-util
Version:        2.1.0
Release:        0%{?dist}
Summary:        ROS swri_route_util package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-marti-common-msgs
Requires:       ros-lunar-marti-nav-msgs
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-swri-geometry-util
Requires:       ros-lunar-swri-math-util
Requires:       ros-lunar-swri-transform-util
Requires:       ros-lunar-visualization-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-marti-common-msgs
BuildRequires:  ros-lunar-marti-nav-msgs
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-swri-geometry-util
BuildRequires:  ros-lunar-swri-math-util
BuildRequires:  ros-lunar-swri-transform-util
BuildRequires:  ros-lunar-visualization-msgs

%description
This library provides functionality to simplify working with the navigation
messages defined in marti_nav_msgs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Jan 26 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.1.0-0
- Autogenerated by Bloom

* Mon Dec 18 2017 Elliot Johnson <elliot.johnson@swri.org> - 2.0.0-0
- Autogenerated by Bloom

* Fri Oct 13 2017 Elliot Johnson <elliot.johnson@swri.org> - 1.2.0-0
- Autogenerated by Bloom

* Thu Aug 31 2017 Elliot Johnson <elliot.johnson@swri.org> - 1.1.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.3.0-0
- Autogenerated by Bloom

