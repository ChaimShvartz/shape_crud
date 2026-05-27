from shape import Shape
from math import pi

class Circle(Shape):
    @property
    def perimeter(self):
        return 2 * pi * self.radius
    
    def get_area(self):
        return self.radius**2 * pi