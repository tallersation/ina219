#!/usr/bin/python3
from ina219 import INA219, DeviceRangeError
import rospy
from std_msgs.msg import String

if __name__ == '__main__' :
    pub = rospy.Publisher('ina_sensor', String, queue_size=10)
    rospy.init_node('ina219')
    rate = rospy.Rate(10)
    ina = INA219(0.1)
    ina.configure()

    while True:
        sensor = [ina.voltage(), ina.current(), ina.power(), ina.shunt_voltage()]
        vcps = "V: %.3f V A: %.3f mA P: %.3f mW SV: %.3f mV" %(sensor[0], sensor[1], sensor[2], sensor[3])
        pub.publish(vcps)
        rate.sleep()


