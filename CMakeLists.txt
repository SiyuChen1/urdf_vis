cmake_minimum_required(VERSION 2.8.3)

project(urdf_vis)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

message("CATKIN_PACKAGE_SHARE_DESTINATION: " ${CATKIN_PACKAGE_SHARE_DESTINATION})
message("CATKIN_GLOBAL_SHARE_DESTINATION: " ${CATKIN_GLOBAL_SHARE_DESTINATION})
message("CMAKE_INSTALL_PREFIX: " ${CMAKE_INSTALL_PREFIX})

foreach(dir images launch meshes rviz urdf)
	message("current directory: "${dir})
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
