# Use platform module to get system information and output it to json and csv files in Documents directory
import platform
import json
import csv
import os

# Get system information
system_info = {
    'system': platform.system(),
    'node': platform.node(),
    'release': platform.release(),
    'version': platform.version(),
    'machine': platform.machine(),
    'processor': platform.processor()
}

# Get user home directory
home_dir = os.path.expanduser('~')

# Set output file path
documents_dir = os.path.join(home_dir, 'Homebase\ScanResults')

# Create json file in documents directory
with open(os.path.join(documents_dir, 'sys_info.json'), 'w') as json_file:
    json.dump(system_info, json_file)

# Create csv file in documents directory
with open(os.path.join(documents_dir, 'sys_info.csv'), 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in system_info.items():
        writer.writerow([key, value])

# Print system information
print(system_info)
