execute_process(COMMAND "/home/mobmonrob/ws_moveit/build/universal_robot/ur_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/mobmonrob/ws_moveit/build/universal_robot/ur_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
