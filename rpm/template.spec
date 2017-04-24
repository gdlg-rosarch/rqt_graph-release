Name:           ros-lunar-rqt-graph
Version:        0.4.8
Release:        0%{?dist}
Summary:        ROS rqt_graph package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_graph
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-lunar-python-qt-binding >= 0.2.19
Requires:       ros-lunar-qt-dotgraph
Requires:       ros-lunar-rosgraph
Requires:       ros-lunar-rosgraph-msgs
Requires:       ros-lunar-roslib
Requires:       ros-lunar-rosnode
Requires:       ros-lunar-rospy
Requires:       ros-lunar-rosservice
Requires:       ros-lunar-rostopic
Requires:       ros-lunar-rqt-gui
Requires:       ros-lunar-rqt-gui-py
BuildRequires:  ros-lunar-catkin

%description
rqt_graph provides a GUI plugin for visualizing the ROS computation graph. Its
components are made generic so that other packages where you want to achieve
graph representation can depend upon this pkg (use rqt_dep to find out the pkgs
that depend. rqt_dep itself depends on rqt_graph too).

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
* Mon Apr 24 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.8-0
- Autogenerated by Bloom

