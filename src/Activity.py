from sense_hat import SenseHat
import time

class Activity:
    def __init__(self, sense):
        self.sense = sense
        self.running = False

    def record(self):
        try:

            self.running = True
            print("Activity started.")
            i = 0
            while self.running:
                # Read data from the IMU
                imu_data = self.sense.get_accelerometer_raw()
                acceleration = imu_data['x'], imu_data['y'], imu_data['z']
                print("Acceleration (g): x={:.2f}, y={:.2f}, z={:.2f}".format(*acceleration))
                time.sleep(0.1)  # Adjust sleep time as needed
                joy_stick = self.sense.stick.get_events()
                for event in joy_stick:
                    if(event.action == "pressed" and event.direction == "middle"):
                        self.running = not self.running
            return "Success"

        except Exception as e:
            return "Failed"

