#Author: Thiarasak Khamyan(UnName)
#Date 27 Oct 2023
#Name: INA219 Sensor ROS2 with Custom Message

import rclpy
from rclpy.node import Node
import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219
from ina219_interface.msg import PowerMessageCommon


class INA219(Node):
    i2c_bus = board.I2C()  # uses board.SCL and board.SDA
    ina219 = INA219(i2c_bus)
    ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
    ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
    ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

    def __init__(self):
        super().__init__('INA219_Sensor')
        self.publisher_ = self.create_publisher(PowerMessageCommon, '/ina219', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = PowerMessageCommon()

        bus_voltage = self.ina219.bus_voltage  # voltage on V- (load side)
        shunt_voltage = self.ina219.shunt_voltage  # voltage between V+ and V- across the shunt
        current = self.ina219.current  # current in mA
        power = self.ina219.power  # power in watts

        msg.vin_p = bus_voltage + shunt_voltage
        msg.vin_n = bus_voltage
        msg.shunt_voltage = shunt_voltage
        msg.shunt_current = current/1000
        msg.power_calc = bus_voltage * (current/1000)
        msg.power_register = power
        if power < 0.01:
            msg.is_pluging = True
        else:
            msg.is_pluging = False
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    ina219 = INA219()

    rclpy.spin(ina219)

    ina219.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()