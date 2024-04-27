import numpy as np
import matplotlib.pyplot as plt
import csv

# Initialize list to store magnitudes
magnitudes = []

# Open and read the CSV file
with open('outputs/50steps.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        # Extract x, y, and z values from each row
        x, y, z = float(row[0]), float(row[1]), float(row[2])
        
        # Calculate magnitude using the provided algorithm
        mag = np.sqrt(x**2 + y**2 + z**2)

        # Append magnitude to the list
        magnitudes.append(mag)

magnitudes = np.array(magnitudes)

with open('outputs/50steps-vectorized.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for mag in magnitudes:
        writer.writerow([mag])