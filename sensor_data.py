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
                'log_format': '{0:0.3f},{1:0.3f},{2:0.3f}',
                'log_name': 'accel_x,accel_y,accel_z',
                'log_unit': 'm/s^2'
            },
            'magnetic': 
            {
                'name': 'magnetic',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.3f},{1:0.3f},{2:0.3f}',
                'log_name': 'mag_x,mag_y,mag_z',
                'log_unit': 'gauss'
            },
            'gyro': 
            {
                'name': 'gyro',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.3f},{1:0.3f},{2:0.3f}',
                'log_name': 'gyro_x,gyro_y,gyro_z',
                'log_unit': 'degrees/sec'
            },
            "temperature":
             {
                'name': 'temperature',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.3f}',
                'log_name': 'temp',
                'log_unit': 'C'
            },
        }
    },
    'bmp3xx': {
        'addresses': ['0x77'],
        'setup_string': adafruit_bmp3xx.BMP3XX_I2C,
        'parameters': {
            'pressure_oversampling': 8,
            'temperature_oversampling': 2,
            'sea_level_pressure':  1013.25
        },
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
                'log_format': '{0:0.3f}',
                'log_name': 'altitude',
                'log_unit': 'meters'
            },
            'pressure' :
            {
                'name': 'pressure',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.3f}',
                'log_name': 'pressure',
                'log_unit': 'hPa'
            },
            'temperature' :
            {
                'name': 'temperature',
                'read': True,
                'value': 0,
                'zero_start': True,
                'smoothing': 0,
                'log_on': True,
                'log_format': '{0:0.3f}',
                'log_name': 'bmp_temperature',
                'log_unit': 'C'
            }
        }
    }
}
