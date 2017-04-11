Name:           ros-jade-swri-nodelet
Version:        0.1.7
Release:        0%{?dist}
Summary:        ROS swri_nodelet package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-nodelet
Requires:       ros-jade-rosbash
Requires:       ros-jade-roscpp
Requires:       ros-jade-std-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-rosbash
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-std-msgs

%description
This package provides a simple script to write simple launch files that can
easily switch between running nodelets together or as standalone nodes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Apr 11 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.1.7-0
- Autogenerated by Bloom

* Sun Oct 23 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.1.6-0
- Autogenerated by Bloom

* Fri May 13 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.1.5-0
- Autogenerated by Bloom

* Thu May 12 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.1.4-0
- Autogenerated by Bloom

