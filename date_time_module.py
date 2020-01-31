#Benefits of learning datatime module
#calculate the difference between today and your birthday
#app that can send emails automatically based on date
#Instagram clone that can say things like "posted 3 days ago"

import datetime
import pytz
today = datetime.date.today()
print(today)
birthday = datetime.date(1995, 6, 27)
print(birthday)

days_since_birth = (today - birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days = 10)
print(today + tdelta)

print(today.month)
print(today.day)
print(today.weekday())
#Monday = 0 to Sunday = 6
#hours min and sec
print(datetime.time(7,2,20,15))
#datetime.date=>(Y,M,D)
#datetime.time=>(Hr,Min,Sec,Ms)
#datetime.datetime => (Y,M,D,Hr,Min,Sec,Ms)

#add 10 hours to current day and time
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

#be aware of timezone. creating timezone
datetime_today = datetime.datetime.now(tz = pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)
#printing all the timezone in the world!
for tz in pytz.all_timezones:
  print(tz)

#string formatting with dates 
#2020-01-31 -> January 31, 2020
#method strftime(f= formatting)
print(datetime_pacific.strftime('%B %d, %Y'))

# January 31, 2020 => datetime object? datetime(2020-01-31)
# method strptime(p = parsing) 
datetime_changing = datetime.datetime.strptime('January 31, 2020', '%B %d, %Y')
print(repr(datetime_changing))

