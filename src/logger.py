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
