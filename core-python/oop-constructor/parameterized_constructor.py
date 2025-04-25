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


s = Shape("Red", 5)

print("Color:", s.getColor())
print("Border Width:", s.getBorderWidth())
