class Rectangle:
    def __init__(self, length, width):
        self.length = length 
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2*(self.length + self.width)