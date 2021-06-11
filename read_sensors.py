def read_sensors(sensor_data):
    for sensor, v in sensor_data.items():
        if(sensor == 'lsm9ds1'):
            if(sensor_data[sensor]['acceleration']['read'] == True):
                sensor_data[sensor]['acceleration']['accel_x']['value'], sensor_data[sensor]['acceleration']['accel_y']['value'], sensor_data[sensor]['acceleration']['accel_z']['value'] = sensor_data[sensor]['device'].acceleration
            if(sensor_data[sensor]['magnetic']['read'] == True):
                sensor_data[sensor]['magnetic']['mag_x']['value'], sensor_data[sensor]['magnetic']['mag_y']['value'], sensor_data[sensor]['magnetic']['mag_z']['value'] = sensor_data[sensor]['device'].magnetic
            if(sensor_data[sensor]['gyro']['read'] == True):
                sensor_data[sensor]['gyro']['gyro_x']['value'], sensor_data[sensor]['gyro']['gyro_y']['value'], sensor_data[sensor]['gyro']['gyro_z']['value'] = sensor_data[sensor]['device'].gyro
    return sensor_data
