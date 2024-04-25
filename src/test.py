
import time
import csv
from pathlib import Path


timestamp = int(time.time())

# Define output file path
output_file_path = Path(f"outputs/{timestamp}.csv").resolve()

with open(output_file_path, 'a') as file:
    for i in range(2):
        file.write("hello" + '\n')
        