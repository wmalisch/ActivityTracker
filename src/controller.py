import time
import numpy as np

from sense_hat import SenseHat

from src.activity import Activity
from src.logger import Logger
from src.sqlite_db_client import SQLiteDBClient

class Controller:
    def __init__(self):
        self.sense = SenseHat()
        self.logger = Logger(self.sense)
        self.activity = Activity(self.sense)
        self.db_client = SQLiteDBClient('Activity.db')
        self.db_client.connect()

    def run(self):
        try:

            # Loop for ever until a user starts recording activities
            while True:
                for event in self.sense.stick.get_events():
                    if event.action == "pressed":

                        # Push inwards to start recording
                        if event.direction == "middle":
                            self.logger.print_start()

                            success = self.activity.record()
                            
                            if success:
                                stats = self.activity.get_latest_activity()
                                self.logger.print_stats(stats)
                            else:
                                self.logger.print_error()
                        
                        # Toggle up to enter view mode
                        elif event.direction == "up":
                            activity_log = self.db_client.get_all()
                            self.view_activities(activity_log)

                # Use a short sleep statement to help save battery. Calls to the SenseHat are battery intensive, this slightly reduces the number of calls
                time.sleep(0.2)

        except KeyboardInterrupt:
            print("Exiting...")
            self.sense.clear()

    # A function to provide users with a view mode. 
    # Using the joy stick, users can toggle through there history of recorded activities
    def view_activities(self, activity_log):
        self.logger.view_mode_on()
        view = True
        print = True
        alog = np.array(activity_log)
        row = 0
        column = 0

        while view:
            if print:
                self.print_current_stat(row, column, alog)
                print = False

            for event in self.sense.stick.get_events():
                if event.action == "pressed":
                    print = True
                    if event.direction == "up" and row > 0:
                        row -= 1
                    elif event.direction == "down" and row < alog.shape[0] - 1:
                        row += 1
                    elif event.direction == "left" and column > 0:
                        column -= 1
                    elif event.direction == "right" and column < alog.shape[1] - 1:
                        column += 1

                    # Press joy stick in the middle to exit view mode
                    elif event.direction == "middle":
                        self.logger.view_mode_off()
                        view = False

            # Use a short sleep statement to help save battery. Calls to the SenseHat are battery intensive, this slightly reduces the number of calls
            time.sleep(0.2)
               
    # A helper function for logging a description and value for the current stat to the LED screen.
    def print_current_stat(self, row, column, activity_log):
        if column == 0:
            message = f"Id: {activity_log[row, column]}"
            self.logger.print_individual_stat_in_activity_log(message)
        elif column == 1:
            message = f"S Date: {activity_log[row, column]}"
            self.logger.print_individual_stat_in_activity_log(message)
        elif column == 2:
            message = f"S Time: {activity_log[row, column]}"
            self.logger.print_individual_stat_in_activity_log(message)
        elif column == 3:
            message = f"Steps: {activity_log[row, column]}"
            self.logger.print_individual_stat_in_activity_log(message)
        elif column == 4:
            message = f"Duration: {activity_log[row, column]}"
            self.logger.print_individual_stat_in_activity_log(message)
        else:
            print("Error")
        