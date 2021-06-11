import pandas as pd
import matplotlib.pyplot as plt

dz = pd.read_csv('datalog.csv', index_col="run_time", usecols = ["run_time", "accel_x", "accel_y", "accel_z"])
dx = pd.read_csv('datalog.csv', index_col="run_time", usecols = ["run_time", "mag_x", "mag_y", "mag_z"])
dy = pd.read_csv('datalog.csv', index_col="run_time", usecols = ["run_time", "gyro_x", "gyro_y", "gyro_z"])

dz.plot()
dx.plot()
dy.plot()


plt.show()
