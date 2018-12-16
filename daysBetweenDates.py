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


## f- modify daysInMonth() to account for leap years
## d- modify daysInMonth() to be correct except for leap years
## c- write stub daysInMonth(year,month) that always return 30
def daysInMonth(year,month):
	"""return the number of days in a given month"""
	if isLeapYear(year) and month == 2:
		return 29
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


## testing modified daysInMonth():
def test():
	"""tests with 30-day months"""
	assert daysBetweenDates(2013,1,1,2013,1,1) == 0
	assert daysBetweenDates(2013,1,1,2013,1,2) == 1
	assert nextDay(2013,1,1) == (2013,1,2)
	assert nextDay(2013,4,30) == (2013,5,1)
	assert nextDay(2012,12,31) == (2013,1,1)
	assert nextDay(2012,12,30) == (2012,12,31)
	assert nextDay(2013,2,28) == (2013,3,1)
	assert nextDay(2012,2,28) == (2012,2,29)
	assert nextDay(2013,9,30) == (2013,10,1)
	assert daysBetweenDates(2012,1,1,2013,1,1) == 366
	assert daysBetweenDates(2013,1,1,2014,1,1) == 365

	print "done"

test()

## final testing:
def test2():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test2()