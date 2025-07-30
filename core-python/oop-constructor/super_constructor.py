class Shape:

    def __init__(self, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color

    def setBorderWidth(self, bw):
        self.borderWidth = bw

    def getBorderWidth(self):
        return self.borderWidth


class Rectangle(Shape):

    def __init__(self, length=0, width=0, color='', borderWidth=0):
        self.length = length
        self.width = width
        super().__init__(color, borderWidth)

    def setLength(self, l):
        self.length = l

    def getLength(self):
        return self.length

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width


# Creating a Rectangle object
r = Rectangle(10, 20, 'red', 100)
print("Rectangle:")
print("Length:", r.getLength())
print("Width:", r.getWidth())
print("Color:", r.getColor())
print("Border Width:", r.getBorderWidth())