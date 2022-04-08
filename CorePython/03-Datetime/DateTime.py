# Example of Date Time 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#
import datetime
#Import the datetime module and display the current date:

# get current datetime 


#print(x.strftime("%A"))


# Get object of given date
x = datetime.datetime(1996, 7, 25)

# format date using strftime() method. Get name of month
print(x.year)
print(x.month)
print(x.day)
print(x.strftime("%y"))
print(x.strftime("%B"))
print(x.strftime("%A"))


