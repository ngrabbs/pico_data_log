def read_sensors(sensor_data):
    for sensor, v in sensor_data.items():
        if(sensor == 'lsm9ds1'):
            if(sensor_data[sensor]['sensors']['acceleration']['read'] == True):
                sensor_data[sensor]['sensors']['acceleration']['value'] = sensor_data[sensor]['device'].acceleration
            if(sensor_data[sensor]['sensors']['magnetic']['read'] == True):
                sensor_data[sensor]['sensors']['magnetic']['value'] = sensor_data[sensor]['device'].magnetic
            if(sensor_data[sensor]['sensors']['gyro']['read'] == True):
                sensor_data[sensor]['sensors']['gyro']['value'] = sensor_data[sensor]['device'].gyro
        elif(sensor == 'bmp3xx'):
           if(sensor_data[sensor]['sensors']['altitude']['read'] == True):
                sensor_data[sensor]['sensors']['altitude']['value'] = sensor_data[sensor]['device'].altitude
           if(sensor_data[sensor]['sensors']['pressure']['read'] == True):
                sensor_data[sensor]['sensors']['pressure']['value'] = sensor_data[sensor]['device'].pressure
    return sensor_data
