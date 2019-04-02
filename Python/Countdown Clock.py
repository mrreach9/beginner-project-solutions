from datetime import datetime, time, date, timedelta
import time

fdate = input("Enter the date you wish to count down to (dd/mm/yyyy):  ")
ftime = input("Enter the time you wish to count down to (hh:mm):  ")

day, month, year = fdate.split('/')
hour, minute = ftime.split(':')
now = datetime.now()
future = datetime(int(year), int(month), int(day), int(hour), int(minute))

diff = future - now

def days_hours_minutes(td):
    date = dict()
    date['days'] = td.days
    date['hours'] = td.seconds//3600
    date['minutes'] = (td.seconds//60)%60
    date['seconds'] = td.seconds % 60
    return date

while True:
    # The below is a tuple and can be accessed via [index]
    time_left = days_hours_minutes(diff)
    print('There are {a} days, {b} hours, {c} minutes, and {d} seconds left until {fdate}(at {ftime})'.format(
            a = time_left['days'], b = time_left['hours'], c = time_left['minutes'], d = time_left['seconds'], fdate = fdate, ftime = ftime))
    time.sleep(5)
    diff -= timedelta(seconds=5)
