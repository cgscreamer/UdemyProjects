import time

print("The epoch on this sysetm starts at" + time.strftime('%c', time.gmtime(0)))
print(" ")
print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
print(" ")
if time.daylight !=0:
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])
print(" ")
print("Local time is " + time.strftime("%Y - %m - %d %H:%M:%S"))