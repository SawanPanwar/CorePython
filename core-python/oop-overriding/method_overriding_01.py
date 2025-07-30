class Shape:

    def area(self):
        print('Shape Area Method')


class Rectangle(Shape):

    def area(self):
        print('Rectangle Area Method')


r = Rectangle()
r.area()

s = Shape()
s.area()

shape:Shape = Rectangle()
shape.area()