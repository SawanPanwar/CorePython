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


s = Shape()
s.setColor("Red")
s.setBorderWidth(5)

print("Color:", s.getColor())
print("Border Width:", s.getBorderWidth())