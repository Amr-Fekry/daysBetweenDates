# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.



## 3- find a simple mechanical solution:

##    3.a work through a few cases.
##        daysBetweenDates(2013,1,24,2013,6,29)
##        daysBetweenDates(2013,1,24,2024,6,29)

##    3.b write a "pseudo code" algorithm:

##    days = 0
##    while date1 is before date2:
##        days += 1
##        date1 = advance to next day

##    simple mechanical solutions are not practical for humans because they will be very time/effort-consuming
##    but they are great for computers which are super fast

##    simple-mechanical solution is easier to write correctly, and saves developer's time and effort but slower on the large scale usage. 
##    complex-shortcut-human solution is faster but it consumes more time and effort to write.
##    depending on the future use of the program, make your trade off between speed and developers time/effort consumed.

##    bottomline: don't optimize prematurely. go with the simple mechanical solution and don't worry about making the algorithm faster until you have to.
