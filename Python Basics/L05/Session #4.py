"""
=========================
-----> Date & Time <-----
=========================
"""
# current date and time
import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())

# current year, month and day
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

# start and end of date
print(datetime.datetime.min)
print(datetime.datetime.max)

# specific date
print(datetime.datetime(2003, 8, 4))
print(datetime.datetime(2003, 8, 4, 5, 20, 17, 1555))

# how long did you live?
birthDate = datetime.datetime(2010, 5, 9)
dateNow = datetime.datetime.now()
print(f'you lived for {(dateNow - birthDate)}')
print(f'you lived for {(dateNow - birthDate).days}')

# https://strftime.org/

myBD = datetime.datetime(2003, 8, 4)
print(myBD)
print(myBD.strftime('%d %b %Y'))
print(myBD.strftime('%a %B %Y'))
