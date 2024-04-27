import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import csv

magnitudes = []

with open('outputs/vectorized_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        # Extract magnitude value from each row
        mag = float(row[0])
        # Append magnitude to the list
        magnitudes.append(mag)

# Convert magnitudes list to numpy array
magnitudes = np.array(magnitudes)

peaks, _ = find_peaks(magnitudes)

plt.plot(magnitudes)
plt.plot(peaks, magnitudes[peaks], "x", color='red')
plt.xlabel('Index')
plt.ylabel('Acceleration Magnitude')
plt.title('Acceleration Magnitude with Peaks')
plt.show()

print("Indices of the peaks:", peaks)