import calendar

# iterweekdays() method	Return an iterator for the weekdays numbers that will be used for one week.
cal= calendar.Calendar(firstweekday=5)
for x in cal.iterweekdays():
	print(x)

# The itermonthdates() method returns an iterator for the month (1-12) in the year.
# This iterator will return all days (as datetime.date objects) for the month and all days before the start of the month or after 
# the end of the month that are required to get a complete week.
cal= calendar.Calendar()
for x in cal.itermonthdates(2016, 5):
	print(x)

# weekday - It gives the day of the week of given date
calendar.setfirstweekday(6)
print(calendar.weekday(2022, 12, 10))

# calendar
print(calendar.calendar(2023))

# leap days
print(calendar.leapdays(2000,2022))

# leap year
print(calendar.isleap(2000))

# months
print(list(calendar.month_name))

# days
print(list(calendar.day_name))
