import datetime

# working with date
d = datetime.date(2022, 12, 10)
print(d)

print(d.year)
print(d.month)
print(d.day)
print(d.isoweekday()) # returns the day index

todays = datetime.date.today()   # returns today's date
print(todays)

todays_in_str = todays.ctime()  # returns string format
print(todays_in_str)

# working with time
t = datetime.time(2, 47, 50, 530000)
print(t)

print(t.hour)
print(t.min)
print(t.second)
print(t.microsecond) 


# working with date and time
todaydt = datetime.datetime(2022, 12, 10, 4, 55, 50, 100000)
print(todaydt)

dt = datetime.datetime.now()    # returns today's date
print(dt)
print(dt.date)
print(dt.time)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.year)
print(dt.month)
print(dt.day)

# timedelta gives the difference
delta = datetime.timedelta(days=5)
new1 = todays + delta
print("new time is ",new1)

new2 = todays - delta
print(new2)

delta = new1-new2
print(delta)

# strf time
print(d.strftime('%A, %B, %d, %Y'))

# format strings
# %a = day name abbreviated
# %A = day name full
# %b = month name abbreviated
# %B = month name full
# %d = date
# %y = year name abbreviated
# %Y = year name full

# strp time
# converts string into date i.e parsing
my_birthday = '2002/11/21'
mybday = datetime.datetime.strptime(my_birthday,'%Y/%m/%d')
print(mybday)
