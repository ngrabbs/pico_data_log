# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time
import board
import busio
import digitalio
import adafruit_lsm9ds1
import adafruit_bmp3xx
from read_sensors import read_sensors
from sensor_data import sensor_data
from logger import logger, init_logger

#led = digitalio.DigitalInOut(board.GP25)
#led.switch_to_output()

# create lsm9ds1 sensor object
i2c0 = busio.I2C(scl=board.GP5, sda=board.GP4)
sensor_data['lsm9ds1']['device'] = adafruit_lsm9ds1.LSM9DS1_I2C(i2c0)

# create bmp3xx sensor object
#i2c1 = busio.I2C(scl=board.GP3, sda=board.GP2)
#sensor_data['bmp3xx']['device'] = adafruit_bmp3xx.xxxxxx(i2c1)

write_log = True
logger_type = 'csv' #mega or csv
log_name = 'datalog.' + logger_type

logger_profile = init_logger(logger_type, sensor_data)

log_time = 10 # in seconds

i = 0
main_start = time.monotonic()
run_time = 0
while run_time < log_time:
    start_read = time.monotonic()
    data = read_sensors(sensor_data)
    run_time = time.monotonic() - main_start
    read_time = time.monotonic() - start_read
    logger(logger_profile, data, run_time, read_time)
    i += 1

