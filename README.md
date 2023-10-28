<h3>This is package for publishing the data from INA219 to ROS2 with Custom Message</h3>


1. Clone INA219-ROS-Package and Clone Custom Message into ROS Workspace<br>
```
cd <ros2_workspace>/src
git clone -b humble https://github.com/tallersation/ina219_interface
git clone -b humble https://githubm.com/tallersation/ina219
```
  - No workspcae! (Use this if there's no workwpace)
    ```
    mkdir -p ff_ros2_ws/src
    cd ff_ros2_ws/src
    git clone -b humble https://github.com/tallersation/ina219_interface
    git clone -b humble https://githubm.com/tallersation/ina219
    ```
2. Build packages using <br>
```
cd ~/<ros2_workspace>/
colcon build --packages-select ina219-msg ina219-pkg
```
 - No workspace! (Use this if there's no workwpace)
   ```
   cd ~/ff_ros2_ws/
   colcon build --packages-select ina219-msg ina219-pkg
   ```
4. Testing <br>
`ros2 run ina219-pkg ina219`
