import matplotlib.pyplot as plt
import csv

# Initialize lists to store data from each column
column1 = []
column2 = []
column3 = []

# Open and read the CSV file
with open('outputs/30steps.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Append data from each column to respective lists
        column1.append(float(row[0]))
        column2.append(float(row[1]))
        column3.append(float(row[2]))

# Plot each column
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(column1, label='Column 1')
plt.plot(column2, label='Column 2')
plt.plot(column3, label='Column 3')

# Add labels and legend
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Data from CSV')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
