# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year): ## a leap year is a multiple of 4 (EXCEPT all hundreds BUT including multiples of 400) 
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    if year % 4 != 0: 
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    ##

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    # days_in_birth_year
    
    days_in_birth_month = daysOfMonths[m1-1] - d1
    
    days_in_rest_of_year = 0
    for days in daysOfMonths[m1:]:
        days_in_rest_of_year += days
    
    days_in_birth_year = days_in_birth_month + days_in_rest_of_year
    
    if isLeapYear(y1):
        if m1 <= 2:
            if d1 <= 28:
                days_in_birth_year += 1
    
    # days_in_years_between
    
    year = y1 + 1
    leap_days = 0
    days_in_years_between = 0
    while year < y2:
        if isLeapYear(y1):
            leap_days += 1
        days_in_years_between += 365
        year += 1 # the risk of using while over for is that you might forget to increment/decrement
    days_in_years_between += leap_days
    
    # days_in_current_year
    
    days_in_months_passed = 0
    for days in daysOfMonths[:m2]:
        days_in_months_passed += days
    
    days_in_current_year = days_in_months_passed + d2
    
    if isLeapYear(y2):
        if m1 > 2:
            days_in_current_year += 1
    
    days = days_in_birth_year + days_in_years_between + days_in_current_year
        
    return days
    
print isLeapYear(800)
print daysBetweenDates(1992, 10, 2, 2018, 8, 11)
print daysBetweenDates(1992, 10, 2, 2018, 8, 11) / 365.