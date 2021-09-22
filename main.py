import os
import csv
import co2meter
from datetime import datetime

mon = co2meter.CO2monitor(bypass_decrypt=True)
data = mon.read_data()

date_str = data[0].strftime('%Y-%m-%d')
time_str = data[0].strftime('%Y-%m-%d %H:%M:%S')

entry = time_str, float(data[1]), float(data[2])

folder = '/home/pi/co2/output'
output_file = date_str + '.csv'
full_path = os.path.join(folder, output_file)

if not os.path.exists(full_path):

    with open(full_path, 'w') as f:

        f.write('Time,Concentration,Temperature\n')

with open(full_path, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(entry)
