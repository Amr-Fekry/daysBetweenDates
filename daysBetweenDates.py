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

## a- write nextDay(year,month,day) function to solve "advance to next day" part of the pseudo code for simple case:
def nextDay(year,month,day):
	"""takes the date of a day and returns the date of the next day (SIMPLE version that assumes all months are 30 days)"""

	day += 1
	if day > 30:
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


## testing daysBetweenDates():
def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

# test assertions:
#print daysBetweenDates(1500,1,1,2000,1,1)
#print daysBetweenDates(2001,1,1,2000,1,1)
