class Logger:
    def __init__(self, sense):
        self.sense = sense

    def print_start(self):
        self.sense.show_message("Go")
        print("Starting activity")

    def print_error(self):
        self.sense.show_message("Error")
        print("An error occured while recording your activity")

    def print_stats(self, activity):
        steps = str(activity[0])
        time = str(activity[1])
        self.sense.show_message(f"Steps: {steps}")
        self.sense.show_message(f"Time: {time}")
        print(activity)

    def print_individual_stat_in_activity_log(self, stat):
        self.sense.show_message(stat)
        print(stat)

    def view_mode_on(self):
        self.sense.show_message("View")
        print("View Mode: On")

    def view_mode_off(self):
        self.sense.show_message("Record")
        print("View Mode: Off")