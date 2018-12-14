# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.



## 1.1- what are the inputs?

## 1.1.a- understand the possible valid inputs:

##      problem states "Given your birthday and the current date" -> {{inputs}} in general: two dates 
##      what are the {{valid inputs}}: (use or make assumptions)
##      * using assumption: "Assume that the birthday and current date are correct dates (and no time travel)" 
##                           -> second date must not be before first date
##      * making assumption: "Assume the dates are valid in the Gregorian calender"
##                           -> both dates are after 15 oct 1582

##      Although program assumptions are requirements for the user to satisfy, 
##      we should be smart and account for users mistakes and use {{defensive programming}} by checking for the assumptions in our code. 

## 1.1.2- decide how to represent inputs:

##      passing them as separate values or grouping/backaging them into objects? up to you.
##      -> we will go with: (year1,month1,day1,year2,month2,day2)
