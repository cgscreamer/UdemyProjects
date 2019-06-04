import pytz
import datetime

country = "Europe/Moscow"
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print("the time in {} is {}".format(country, local_time))

for x in pytz.all_timezones:
    print(x)