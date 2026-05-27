from shape import Shape
from math import sqrt

class Hexagon(Shape):
    @property
    def area(self):
        return 3 * sqrt(3) * self.side**2 / 2
    
    @property
    def perimeter(self):
        return self.side * 6