import numpy as np
import matplotlib.pyplot as plt
import csv

# Initialize list to store magnitudes
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

# Plot magnitudes
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(magnitudes, label='Magnitude')
plt.xlabel('Index')
plt.ylabel('Magnitude')
plt.title('Magnitude from vectorized_data.csv')
plt.legend()
plt.grid(True)
plt.show()