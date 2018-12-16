# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.



## 4- develop incrementally (small bits of code) and TEST as you go:
##    start breaking down the problem into small parts and make progress

##    "pseudo code" algorithm:

##    days = 0
##    while date1 is before date2:
##        days += 1
##        date1 = advance to next day 


## e- define isLeapYear(year)
## a leap year is a multiple of 4 (EXCEPT all hundreds BUT including multiples of 400)
def isLeapYear(year): 
	"""returns True if year is leap and False if not"""

	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	else:
		return False


## d- modify daysInMonth() to be correct except for leap years
## c- write stub daysInMonth(year,month) that always return 30
def daysInMonth(year,month):
	"""return the number of days in a given month"""
	daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	return daysOfMonths[month - 1]

## c.2 modify nextDay() to use daysInMonth()
## a- write nextDay(year,month,day) function to solve "advance to next day" part of the pseudo code for simple case:
def nextDay(year,month,day):
	"""takes the date of a day and returns the date of the next day (SIMPLE version that assumes all months are 30 days)"""

	day += 1
	if day > daysInMonth(year,month):
		day = 1
		month += 1
		if month > 12:
			month = 1
			year += 1
	return year, month, day

## b.1 define a helper function dateIsBefore() to evaluate the loop condition "date1 is before date2":  
def dateIsBefore(year1,month1,day1,year2,month2,day2):
	"""takes two dates and returns True/False depending on whether first date is before the second"""

	if (year1 < year2) or (year1 == year2 and month1 < month2) or (year1 == year2 and month1 == month2 and day1 < day2):
		return True
	return False

## b- define daysBetweenDates(year1,month1,day1,year2,month2,day2) to give approximate answers:
def daysBetweenDates(year1,month1,day1,year2,month2,day2):
	"""takes two dates and returns the number of days between them"""

	# assert date1 is before date2 and they are valid dates in Gregorian calendar
	assert not dateIsBefore(year2,month2,day2,year1,month1,day1)
	assert not dateIsBefore(year1,month1,day1,1582,10,15)

	days = 0
	while dateIsBefore(year1,month1,day1,year2,month2,day2):
		days += 1
		year1,month1,day1 = nextDay(year1,month1,day1)
	return days


## testing isLeapYear():

print isLeapYear(4)
print isLeapYear(80)
print isLeapYear(100)
print isLeapYear(300)
print isLeapYear(1200)
print isLeapYear(1204)
