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

mean_value = np.mean(magnitudes)
std_dev = np.std(magnitudes)

# Plot magnitudes
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(magnitudes, label='Magnitude')
plt.xlabel('Index')
plt.ylabel('Magnitude')
plt.title('Magnitude from vectorized_data.csv')

# Plot mean and standard deviation lines
plt.axhline(mean_value, color='r', linestyle='--', label='Mean')
plt.axhline(mean_value + std_dev*1.5, color='g', linestyle='--', label='Mean + StdDev')
plt.axhline(mean_value - std_dev*1.5, color='g', linestyle='--', label='Mean - StdDev')

# Annotate mean and standard deviation values
plt.text(0.5, mean_value, f'Mean: {mean_value:.2f}', color='r', fontsize=10, va='center', ha='left')
plt.text(0.5, mean_value + std_dev, f'Standard Deviation: {std_dev:.2f}', color='g', fontsize=10, va='center', ha='left')
plt.text(0.5, mean_value - std_dev, f'Standard Deviation: {std_dev:.2f}', color='g', fontsize=10, va='center', ha='left')

plt.legend()
plt.grid(True)
plt.show()
