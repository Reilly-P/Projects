# My name is Reilly Prescott and this is my Rectangle Class Program
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x = 0, y = 0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):   
      return "({0}, {1})".format(self.x, self.y)

class Rectangle:
    """ A class to manufacture rectangle objects """
    
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h
    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height
    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy
    def perimeter(self):    
        return (self.width+ self.height)*2
    def area(self):
        return (self.width*self.height)
    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
r = Rectangle(Point(0, 0), 10, 5)
assert(r.area() == 50)
r = Rectangle(Point(0, 0), 10, 5)
assert(r.perimeter() == 30)

