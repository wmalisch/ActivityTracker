import numpy as np
import time
import csv
import pytz

from scipy.signal import find_peaks
from src.sqlite_db_client import SQLiteDBClient
from pathlib import Path
from datetime import datetime

class Activity:
    def __init__(self, sense):
        self.sense = sense
        self.db_client = SQLiteDBClient('Activity.db')
        self.db_client.connect()
        self.est_timezone = pytz.timezone('US/Eastern')

    def record(self):
        try:
            self.running = True
            magnitudes = []

            # Get start time
            utc_start = datetime.now(pytz.utc)
            est_start = utc_start.astimezone(self.est_timezone)

            # Extract the date and time components
            start_date = est_start.strftime('%Y-%m-%d')
            start_time = est_start.strftime('%H:%M:%S')

            # Write accelerometer data to disk as a default in case we need to back it up later
            timestamp = int(time.time())
            output_file_path = Path(f"outputs/{timestamp}.csv").resolve()
            with open(output_file_path, 'a') as file:
                
                writer = csv.writer(file)

                while self.running:
                    # Read data from the IMU
                    imu_data = self.sense.get_accelerometer_raw()
                    acceleration = imu_data['x'], imu_data['y'], imu_data['z']

                    # Append accelerometer data raw to the current recording's file on disk. Vectorize.py can be used to conver this data later if needed.
                    rounded_acceleration = [round(value, 2) for value in acceleration]
                    writer.writerow(rounded_acceleration)
                    
                    # Calculate magnitude using the provided algorithm
                    mag = np.sqrt(float(acceleration[0])**2 + float(acceleration[1])**2 + float(acceleration[2])**2)
                    magnitudes.append(mag)

                    # Every iteration, check if the user has ended recording by toggling the joy stick
                    joy_stick = self.sense.stick.get_events()
                    for event in joy_stick:
                        if(event.action == "pressed" and event.direction == "middle"):
                            self.running = not self.running

                    # Sleep statement helps quiet the noise in the data. 
                    # Without this, we over estimate the number of steps
                    time.sleep(0.1)

            # Convert to a numpy array, so we can leverage the find_peaks function from scipy
            magnitudes = np.array(magnitudes)

            # Calc std_dev and mean. We use these to derive a minimum threshold for considering accelerometer fluctuations as a step
            std_dev = np.std(magnitudes) * 0.5
            mean = np.mean(magnitudes)

            # Calculate the peaks - these are steps!
            steps, _ = find_peaks(magnitudes, height=(std_dev + mean))
            
            # Update SQLite database with the recorded activity\
            utc_end = datetime.now(pytz.utc)
            est_end = utc_end.astimezone(self.est_timezone)
            end_date = est_end.strftime('%Y-%m-%d')
            end_time = est_end.strftime('%H:%M:%S')
            
            steps_count = len(steps)
            self.db_client.insert_activity_entry(start_date, start_time, end_date, end_time, steps_count)

            return True

        except Exception as e:
            print(e, "An error was encountered when recording your activity. Please try again.")
            return False

    def get_latest_activity(self):
        return self.db_client.get_latest_activity()