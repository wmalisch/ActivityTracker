# Logger.py

class Logger:
    def __init__(self, sense):
        self.sense = sense

    def print_start(self):
        self.sense.show_message("Go")

    def print_end(self):
        self.sense.show_message("End")

    def print_stats(self, temperature, humidity, pressure):
        stats_message = "Temp: {:.1f}C Humidity: {:.1f}% Pressure: {:.1f}mb".format(temperature, humidity, pressure)
        self.sense.show_message(stats_message)
