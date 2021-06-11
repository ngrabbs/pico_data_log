def init_sensors(i2c0, sensor_data):
    # Lock the I2C device before we try to scan
    while not i2c0.try_lock():
        pass
    i2c_addresses = i2c0.scan()
    i2c0.unlock()

    for device_address in i2c_addresses:
        for k in sensor_data:
            if(hex(device_address) in sensor_data[k]['addresses']):
                sensor_data[k]['device'] = sensor_data[k]['setup_string'](i2c0)
    return sensor_data
