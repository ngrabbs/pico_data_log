# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time
import board
import busio
import digitalio
import adafruit_lsm9ds1
from read_sensors import read_sensors
from sensor_data import sensor_data
from logger import logger, init_logger

#led = digitalio.DigitalInOut(board.GP25)
#led.switch_to_output()

# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(scl=board.GP5, sda=board.GP4)  # uses board.SCL and board.SDA
sensor_data['lsm9ds1']['device'] = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

write_log = True
logger_type = 'csv' #mega or csv
log_name = 'datalog.' + logger_type

logger_profile = init_logger(logger_type, sensor_data)

cycles = 100

i = 0
main_start = time.monotonic()
while i < cycles:
    start_read = time.monotonic()
    data = read_sensors(sensor_data)
    run_time = time.monotonic() - main_start
    read_time = time.monotonic() - start_read

    logger(logger_profile, data, run_time, read_time)
    i += 1
