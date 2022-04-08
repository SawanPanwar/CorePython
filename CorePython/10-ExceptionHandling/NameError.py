# Example of simple Try Except with NameError
# 
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  

#The try block will generate a NameError, because Ram is not defined:
try:
    print("name")
except NameError as e:
  print("Exceptio", e)
except:
  print("Something else went wrong")
