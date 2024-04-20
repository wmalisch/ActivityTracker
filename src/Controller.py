# Controller.py

from src.Activity import Activity
from src.Logger import Logger
from sense_hat import SenseHat

class Controller:
    def __init__(self):
        self.sense = SenseHat()
        self.logger = Logger(self.sense)
        self.activity = Activity(self.sense)

    def run(self):
        try:
            while True:
                for event in self.sense.stick.get_events():
                    if event.action == "pressed":
                        if event.direction == "middle":
                            self.logger.print_start()
                            status = self.activity.record()
                            print(status)
                            self.logger.print_end()

        except KeyboardInterrupt:
            print("Exiting...")
            self.sense.clear()
