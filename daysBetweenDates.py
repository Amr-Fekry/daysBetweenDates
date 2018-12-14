# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.



## 2- think about how to systematically solve the problem as a human:

##    2.a work through a few cases in a systematic way as a human.
##        daysBetweenDates(2013,1,24,2013,6,29)
##        daysBetweenDates(2013,1,24,2024,6,29)

##    2.b write a "pseudo code" algorithm that systematizes how you solved the problem as a human.

##    algorithm pseudo code:

##    days = no. of days in month1 - day1 (31-24=7)
##    month1 += 1
##    while month1 < month2:
##        days += no. of days in month1
##        month1 += 1
##    days += day2
##    while year1 < year2:
##        days += days in year1
##        year1 += 1

##    2.c decide whether you should implement this algorithm?
##        No. it is already complex and it doesn't handle all the cases
##        it doesn't handle:
##        - input dates in same month
##        -  month2 < month1, year2 > year1
##        -  counting days in leap years

##        we should try to find a simpler way (simple, mechanical solution)
