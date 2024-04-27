import pytz
from datetime import datetime

# Get the current date and time (in UTC)
utc_now = datetime.now(pytz.utc)

# Create a timezone object for Eastern Standard Time (EST)
est_timezone = pytz.timezone('US/Eastern')

# Localize the current time to Eastern Standard Time (EST)
est_now = utc_now.astimezone(est_timezone)

# Extract the date and time components
start_date = est_now.strftime('%Y-%m-%d')
start_time = est_now.strftime('%H:%M:%S')

print("Current date in EST:", start_date)
print("Current time in EST:", start_time)
