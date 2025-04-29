# Base class
from typing import List


class Shape:

    def area(self):
        print('Shape Area Method')


# Child class overriding area()
class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.width = 0

    def setLength(self, l):
        self.length = l

    def getLength(self):
        return self.length

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width

    def area(self):
        rectangle_area = self.length * self.width
        print('Rectangle Area:', rectangle_area)
        return rectangle_area


# Another child class overriding area()
class Circle(Shape):
    PI = 3.14  # Class-level constant

    def __init__(self):
        self.radius = 0

    def setRadius(self, r):
        self.radius = r

    def getRadius(self):
        return self.radius

    def area(self):
        circle_area = self.PI * self.radius * self.radius
        print('Circle Area:', circle_area)
        return circle_area


# Define a list of Shape objects
shapes: List[Shape] = [Rectangle(), Circle()]

rect: Rectangle = shapes[0]
rect.setLength(10)
rect.setWidth(20)

cir: Circle = shapes[1]
cir.setRadius(10)

# Loop over the list and call area
for shape in shapes:
    shape.area()

# shape: Shape = Rectangle()
# rectangle: Rectangle = shape
# rectangle.setLength(10)
# rectangle.setWidth(20)
# shape.area()