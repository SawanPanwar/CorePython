class Shape:

    def __init__(self):
        self._color = ''  # protected variable
        self._borderWidth = 0  # protected variable

    def setColor(self, c):
        self._color = c  # setter method

    def getColor(self):
        return self._color  # getter method

    def setBorderWidth(self, bw):
        self._borderWidth = bw  # setter method

    def getBorderWidth(self):
        return self._borderWidth  # getter method


# Test
s = Shape()
s.setColor("Red")
s.setBorderWidth(5)

print("Color:", s.getColor())
print("Border Width:", s.getBorderWidth())

# Accessing the protected variables directly (not recommended, but possible)
print("Protected color directly:", s._color)  # This is allowed but not encouraged