from shape import Shape

class Triangle(Shape):
    @property
    def area(self):
        return self.width * self.height / 2
    
    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c