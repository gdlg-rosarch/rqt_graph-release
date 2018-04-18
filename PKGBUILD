# Script generated with Bloom
pkgdesc="ROS - rqt_graph provides a GUI plugin for visualizing the ROS computation graph.<br/> Its components are made generic so that other packages where you want to achieve graph representation can depend upon this pkg (use <a href="http://www.ros.org/wiki/rqt_dep">rqt_dep</a> to find out the pkgs that depend. rqt_dep itself depends on rqt_graph too)."
url='http://wiki.ros.org/rqt_graph'

pkgname='ros-melodic-rqt-graph'
pkgver='0.4.9_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-catkin'
)

depends=('python2-rospkg'
'ros-melodic-python-qt-binding>=0.2.19'
'ros-melodic-qt-dotgraph'
'ros-melodic-rosgraph'
'ros-melodic-rosgraph-msgs'
'ros-melodic-roslib'
'ros-melodic-rosnode'
'ros-melodic-rospy'
'ros-melodic-rosservice'
'ros-melodic-rostopic'
'ros-melodic-rqt-gui'
'ros-melodic-rqt-gui-py'
)

conflicts=()
replaces=()

_dir=rqt_graph
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_graph $srcdir/rqt_graph
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

