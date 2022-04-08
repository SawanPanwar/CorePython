from builtins import print

from Shape import *
from Circle import *
from Triangle import *
from Rectangle import *

r = Rectangle(5, 5)
c = Circle(3)
t = Triangle(2, 5)
s = Shape("red", 5)
print(r.area())
print("str = ",r)
print(c.area())
print(t.area())
print(s.area())
