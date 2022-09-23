#!/usr/bin/python3
from ina219 import INA219, DeviceRangeError
import rospy
from std_msgs.msg import String

try:
    pub = rospy.Publisher('ina_sensor', String, queue_size=10)
    rospy.init_node('ina219')
    rate = rospy.Rate(10)
    ina = INA219(0.1)
    ina.configure()

    while not rospy.is_shutdown():
        sensor = [ina.voltage(), ina.current(), ina.power(), ina.shunt_voltage()]
        vcps = "V: %.3f V A: %.3f mA P: %.3f mW SV: %.3f mV" %(sensor[0], sensor[1], sensor[2], sensor[3])
        pub.publish(vcps)
        rate.sleep()
except:
    pass


