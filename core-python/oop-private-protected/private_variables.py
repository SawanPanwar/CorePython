class Shape:

    def __init__(self):
        self.__color = ''  # private variable
        self.__borderWidth = 0  # private variable

    def setColor(self, c):
        self.__color = c  # setter method

    def getColor(self):
        return self.__color  # getter method

    def setBorderWidth(self, bw):
        self.__borderWidth = bw  # setter method

    def getBorderWidth(self):
        return self.__borderWidth  # getter method


s = Shape()
s.setColor("Red")
s.setBorderWidth(5)

print("Color:", s.getColor())
print("Border Width:", s.getBorderWidth())
