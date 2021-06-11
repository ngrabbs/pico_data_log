sensor_data = {
    'lsm9ds1': {
        'device': '',
        'acceleration': {
            'read': True,
            'accel_x': {
                'value': 0,
                'source': 'blah',
                'is_active': True,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '0.4f',
                'log_name': 'accel_x',
                'log_unit': 'm/s'
            },
            'accel_y': {
                'value': 0,
                'source': 'blah',
                'is_active': False,
                'zero_start': False,
                'smoothing': 0,
                'log_on': True,
                'log_format': '0.4f',
                'log_name': 'accel_y',
                'log_unit': 'm/s'
        
            },
            'accel_z': {
                'value': 0,
                'source': 'blah',
                'is_active': False,
                'zero_start': False,
                'smoothing': 0,
                'log_on': True,
                'log_format': '0.4f',
                'log_name': 'accel_z',
                'log_unit': 'm/s'
        
            }
        },
        'magnetic': {
            'read': True,
            'mag_x': {
                'source': 'blah',
                'is_active': True,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '0.4f',
                'log_name': 'mag_x',
                'log_unit': 'm/s'
            },
            'mag_y': {
                'source': 'blah',
                'is_active': False,
                'zero_start': False,
                'smoothing': 0,
                'log_on': True,
                'log_format': '0.4f',
                'log_name': 'mag_y',
                'log_unit': 'm/s'
            },
            'mag_z': {
                'source': 'blah',
                'is_active': False,
                'zero_start': False,
                'smoothing': 0,
                'log_on': True,
                'log_format': '0.4f',
                'log_name': 'mag_z',
                'log_unit': 'm/s'
            }
        },
        'gyro': {
            'read': True,
            'gyro_x': {
                'source': 'blah',
                'is_active': True,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '0.4f',
                'log_name': 'gyro_x',
                'log_unit': 'm/s'
        
            },
            'gyro_y': {
                'source': 'blah',
                'is_active': False,
                'zero_start': False,
                'smoothing': 0,
                'log_on': True,
                'log_format': '0.4f',
                'log_name': 'gyro_y',
                'log_unit': 'm/s'
            },
            'gyro_z': {
                'source': 'blah',
                'is_active': False,
                'zero_start': False,
                'smoothing': 0,
                'log_on': True,
                'log_format': '0.4f',
                'log_name': 'gyro_z',
                'log_unit': 'm/s'
            }
        },
        'temperature': {
            'read': False
        }
    }
}

#print(sensor_data);

#for k, v in sensor_data.items():
#    print(k)
