class Shape:
    def __init__(self):
        self.color = ''
        self.borderWidth = 0

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color

    def setBorderWidth(self, bw):
        self.borderWidth = bw

    def getBorderWidth(self):
        return self.borderWidth


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


# Test
r = Rectangle()
r.setLength(10)
r.setWidth(20)
r.setColor("red")
r.setBorderWidth(100)

print("Length:", r.getLength())
print("Width:", r.getWidth())
print("Color:", r.getColor())
print("Border Width:", r.getBorderWidth())
