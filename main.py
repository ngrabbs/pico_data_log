# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time
import board
import busio
import digitalio
#import adafruit_lsm9ds1
import adafruit_bmp3xx
from read_sensors import read_sensors
from sensor_data import sensor_data
from logger import logger, init_logger
from init_sensors import init_sensors

#led = digitalio.DigitalInOut(board.GP25)
#led.switch_to_output()

#init bus
i2c0 = busio.I2C(scl=board.GP5, sda=board.GP4)

sensor_data = init_sensors(i2c0, sensor_data)

write_log = True
logger_type = 'csv' #mega or csv
log_name = 'datalog.' + logger_type
logger_profile = init_logger(logger_type, sensor_data)
log_time = 1 # in seconds

main_start = time.monotonic()
run_time = 0
while run_time < log_time:
    start_read = time.monotonic()
    data = read_sensors(sensor_data)
    run_time = time.monotonic() - main_start
    read_time = time.monotonic() - start_read
    logger(logger_profile, data, run_time, read_time)
