import time

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
            while True:
                for event in self.sense.stick.get_events():
                    if event.action == "pressed":
                        if event.direction == "middle":
                            self.logger.print_start()

                            success = self.activity.record()
                            
                            if success:
                                stats = self.activity.get_latest_activity()
                                self.logger.print_stats(stats)
                            else:
                                self.logger.print_error()
                        
                        elif event.direction == "up":
                            activity_log = self.db_client.get_all()
                            self.view_activities(activity_log)

                # Use a short sleep statement to help save battery. Calls to the SenseHat are battery intensive, this slightly reduces the number of calls
                time.sleep(0.1)

        except KeyboardInterrupt:
            print("Exiting...")
            self.sense.clear()

    def view_activities(self, activity_log):
        print(activity_log)