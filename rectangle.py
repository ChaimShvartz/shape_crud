from shape import Shape

class Rectangle(Shape):
    @property
    def area(self):
        return self.height * self.width
    
    @property
    def perimeter(self):
        return (self.width + self.height) * 2