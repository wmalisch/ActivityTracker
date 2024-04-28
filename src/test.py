import pytz
from datetime import datetime
import time

# Get the current date and time (in UTC)
utc_start = datetime.now(pytz.utc)

# Create a timezone object for Eastern Standard Time (EST)
est_timezone = pytz.timezone('US/Eastern')

# Localize the current time to Eastern Standard Time (EST)
est_now = utc_start.astimezone(est_timezone)

# Extract the date and time components
start_date = est_now.strftime('%Y-%m-%d')
start_time = est_now.strftime('%H:%M:%S')

print("Current date in EST:", start_date)
print("Current time in EST:", start_time)

time.sleep(1)



utc_end = datetime.now(pytz.utc)
# Create a timezone object for Eastern Standard Time (EST)
est_timezone = pytz.timezone('US/Eastern')

# Localize the current time to Eastern Standard Time (EST)
est_now = utc_end.astimezone(est_timezone)
end_time = est_now.strftime('%H:%M:%S')
print(end_time)