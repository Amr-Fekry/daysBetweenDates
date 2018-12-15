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

'''
## instructor solution:
def nextDay(year,month,day):
	""""""
	if day < 30:
		return year, month, day + 1
	elif month < 12:
		return year, month + 1, 1
	else:
		return year + 1, 1, 1
'''

## testing
print nextDay(1992, 10, 1) # (1992, 10, 2)
print nextDay(1999, 12, 30) # (2000, 1, 1)
print nextDay(2013, 1, 30) # (2013, 2, 1)
print nextDay(2012, 12, 30) # (2013, 1, 1)
