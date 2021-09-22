%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-swri-image-util
Version:        3.3.2
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS swri_image_util package

License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       eigen3-devel
Requires:       ros-rolling-ament-index-cpp
Requires:       ros-rolling-camera-calibration-parsers
Requires:       ros-rolling-cv-bridge
Requires:       ros-rolling-geometry-msgs
Requires:       ros-rolling-image-geometry
Requires:       ros-rolling-image-transport
Requires:       ros-rolling-message-filters
Requires:       ros-rolling-nav-msgs
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclcpp-components
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-swri-geometry-util
Requires:       ros-rolling-swri-math-util
Requires:       ros-rolling-swri-opencv-util
Requires:       ros-rolling-swri-roscpp
Requires:       ros-rolling-tf2
Requires:       ros-rolling-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  eigen3-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-index-cpp
BuildRequires:  ros-rolling-camera-calibration-parsers
BuildRequires:  ros-rolling-cv-bridge
BuildRequires:  ros-rolling-geometry-msgs
BuildRequires:  ros-rolling-image-geometry
BuildRequires:  ros-rolling-image-transport
BuildRequires:  ros-rolling-message-filters
BuildRequires:  ros-rolling-nav-msgs
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclcpp-components
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-swri-geometry-util
BuildRequires:  ros-rolling-swri-math-util
BuildRequires:  ros-rolling-swri-opencv-util
BuildRequires:  ros-rolling-swri-roscpp
BuildRequires:  ros-rolling-tf2
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
swri_image_util

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Sep 22 2021 P. J. Reed <preed@swri.org> - 3.3.2-2
- Autogenerated by Bloom

* Wed Sep 08 2021 P. J. Reed <preed@swri.org> - 3.3.2-1
- Autogenerated by Bloom

