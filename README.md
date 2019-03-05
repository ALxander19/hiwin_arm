# hiwin_arm
Steps to load the robot and the IK

1. Copy or download the packages in the your ros workspace
2. go to the folder where is you workspace, for example:

$ cd ros_ws

3. Instance all the package with catkin

/ros_ws$ catkin_make

4. run the roslaunch for moveit

/ros_ws$ roslaunch hiwin_moveit demo.launch

5. Run the demostration for the plane XY

/ros_ws$ rosrun arm_control planexy.py
