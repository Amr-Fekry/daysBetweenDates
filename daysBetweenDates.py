# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old. 


def isLeapYear(year): 
	"""returns True if year is leap. otherwise, False"""

	# a leap year is a multiple of 4 (EXCEPT all hundreds BUT including multiples of 400)
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	else:
		return False

def daysInMonth(year,month):
	"""returns the number of days in a given month, taking leap years into account"""
	if isLeapYear(year) and month == 2:
		return 29
	daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	return daysOfMonths[month - 1]

def nextDay(year,month,day):
	"""returns the date of the day next to year-month-day"""
	day += 1
	if day > daysInMonth(year,month):
		day = 1
		month += 1
		if month > 12:
			month = 1
			year += 1
	return year, month, day

def dateIsBefore(year1,month1,day1,year2,month2,day2):
	"""returns True if year1-month1-day1 is before year2-month2-day2. otherwise, False"""
	if (year1 < year2) or (year1 == year2 and month1 < month2) or (year1 == year2 and month1 == month2 and day1 < day2):
		return True
	return False

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
	"""returns number of days between two dates"""

	# assert date1 is before date2 
	assert not dateIsBefore(year2,month2,day2,year1,month1,day1)
	# assert date1 is valid in the Gregorian calendar
	assert not dateIsBefore(year1,month1,day1,1582,10,15)

	days = 0
	while dateIsBefore(year1,month1,day1,year2,month2,day2):
		days += 1
		year1,month1,day1 = nextDay(year1,month1,day1)
	return days
