# Controller.py

from src.Logger import Logger
from sense_hat import SenseHat

class Controller:
    def __init__(self):
        self.sense = SenseHat()
        self.logger = Logger(self.sense)
        self.recording = False

    def run(self):
        try:
            while True:
                for event in self.sense.stick.get_events():
                    if event.action == "pressed":
                        if event.direction == "middle" and not self.recording:
                            self.logger.print_start()
                            self.recording = not self.recording
                        elif event.direction == "middle" and self.recording:
                            self.logger.print_end()
                            print(event)
                            self.recording = not self.recording

        except KeyboardInterrupt:
            print("Exiting...")
            self.sense.clear()
