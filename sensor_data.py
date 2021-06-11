import adafruit_lsm9ds1
import adafruit_bmp3xx
sensor_data = {
    'lsm9ds1': {
        'addresses': ['0x6b'],
        'setup_string': adafruit_lsm9ds1.LSM9DS1_I2C,
        'device': '',
        'sensors': {
            'acceleration': 
            {
                'name': 'acceleration',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.4f},{1:0.4f},{2:0.4f}',
                'log_name': 'accel_x,accel_y,accel_z',
                'log_unit': 'm/s'
            },
            'magnetic': 
            {
                'name': 'magnetic',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.4f},{1:0.4f},{2:0.4f}',
                'log_name': 'mag_x,mag_y,mag_z',
                'log_unit': 'm/s'
            },
            'gyro': 
            {
                'name': 'gyro',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.4f},{1:0.4f},{2:0.4f}',
                'log_name': 'gyro_x,gyro_y,gyro_z',
                'log_unit': 'm/s'
            }
        }
    },
    'bmp3xx': {
        'addresses': ['0x77'],
        'setup_string': adafruit_bmp3xx.BMP3XX_I2C,
        'device': '',
        'sensors':{
            'altitude' :
            {
                'name': 'altitude',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.4}',
                'log_name': 'altitude',
                'log_unit': 'm'
            },
            'pressure' :
            {
                'name': 'pressure',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.4f}',
                'log_name': 'pressure',
                'log_unit': 'psi'
            }
        }
    }
}
