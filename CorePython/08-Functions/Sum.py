def sumnum( a, *varg ):
   t = a
   print(t)
   for i in varg:
      print("t = ", t, "i = ", i)
      t+=i
   return t;

total = sumnum(2,2,3,4,5)
print('Total', total)
