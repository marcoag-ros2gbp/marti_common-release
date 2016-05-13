Name:           ros-indigo-swri-geometry-util
Version:        0.0.11
Release:        0%{?dist}
Summary:        ROS swri_geometry_util package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       geos-devel
Requires:       opencv-devel
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  eigen3-devel
BuildRequires:  geos-devel
BuildRequires:  opencv-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf

%description
swri_geometry_util

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
* Fri May 13 2016 Marc Alban <malban@swri.org> - 0.0.11-0
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-3
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-2
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-1
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-0
- Autogenerated by Bloom

