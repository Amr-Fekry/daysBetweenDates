# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.



## 1.3- understand the relationship between inputs and outputs by working out some examples. 

##      function(inputs) -> output
        
##      daysBetweenDates(2012, 12, 7, 2012, 12, 7) -> 0 
##      daysBetweenDates(2012, 12, 7, 2012, 12, 8) -> 1
##      daysBetweenDates(2012, 12, 8, 2012, 12, 7) -> undefined (error message: date 1 is after date 2)
##      daysBetweenDates(2012, 6, 29, 2013, 6, 29) -> 365
##      daysBetweenDates(2012, 6, 29, 2013, 6, 31) -> undefined (error message: June is 30 days)
