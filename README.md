# INA219 Package for turtlebot3 

INA219 connected by I2C directly with Raspberry Pi 4

Before run launch file. Please enable I2C first and change permission for /dev/i2c*


Git clone the package:
```
cd ~/catkin_ws/src
git clone https://github.com/tallersation/ina219.git ina219   
cd ~/catkin_ws/catkin_make
```


INA219 Library Installation Commands:
```sudo pip3 install pi-ina219```


Commands:
```sudo chmod 777 /dev/i2c*```
