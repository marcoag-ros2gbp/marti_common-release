%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-swri-transform-util
Version:        3.5.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS swri_transform_util package

License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       geos-devel
Requires:       proj-devel
Requires:       python%{python3_pkgversion}-numpy
Requires:       ros-humble-cv-bridge
Requires:       ros-humble-diagnostic-msgs
Requires:       ros-humble-diagnostic-updater
Requires:       ros-humble-geographic-msgs
Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-gps-msgs
Requires:       ros-humble-launch-xml
Requires:       ros-humble-marti-nav-msgs
Requires:       ros-humble-rcl-interfaces
Requires:       ros-humble-rclcpp
Requires:       ros-humble-rclcpp-components
Requires:       ros-humble-rclpy
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-swri-math-util
Requires:       ros-humble-swri-roscpp
Requires:       ros-humble-tf2
Requires:       ros-humble-tf2-geometry-msgs
Requires:       ros-humble-tf2-py
Requires:       ros-humble-tf2-ros
Requires:       yaml-cpp-devel
Requires:       ros-humble-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  geos-devel
BuildRequires:  pkgconfig
BuildRequires:  proj-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ament-cmake-python
BuildRequires:  ros-humble-cv-bridge
BuildRequires:  ros-humble-diagnostic-msgs
BuildRequires:  ros-humble-diagnostic-updater
BuildRequires:  ros-humble-geographic-msgs
BuildRequires:  ros-humble-geometry-msgs
BuildRequires:  ros-humble-gps-msgs
BuildRequires:  ros-humble-marti-nav-msgs
BuildRequires:  ros-humble-rcl-interfaces
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rclcpp-components
BuildRequires:  ros-humble-rclpy
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-swri-math-util
BuildRequires:  ros-humble-swri-roscpp
BuildRequires:  ros-humble-tf2
BuildRequires:  ros-humble-tf2-geometry-msgs
BuildRequires:  ros-humble-tf2-ros
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The swri_transform_util package contains utility functions and classes for
transforming between coordinate frames.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Thu Nov 03 2022 P. J. Reed <preed@swri.org> - 3.5.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 P. J. Reed <preed@swri.org> - 3.4.0-3
- Autogenerated by Bloom

* Tue Feb 08 2022 P. J. Reed <preed@swri.org> - 3.4.0-2
- Autogenerated by Bloom

