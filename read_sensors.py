def read_sensors(sensor_data):
    for sensor, v in sensor_data.items():
        if(sensor == 'lsm9ds1'):
            if(sensor_data[sensor]['sensors']['acceleration']['read'] == True):
                sensor_data[sensor]['sensors']['acceleration']['value'] = sensor_data[sensor]['device'].acceleration
            if(sensor_data[sensor]['sensors']['magnetic']['read'] == True):
                sensor_data[sensor]['sensors']['magnetic']['value'] = sensor_data[sensor]['device'].magnetic
            if(sensor_data[sensor]['sensors']['gyro']['read'] == True):
                sensor_data[sensor]['sensors']['gyro']['value'] = sensor_data[sensor]['device'].gyro
    return sensor_data
