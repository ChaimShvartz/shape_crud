from shape import Shape

class Square(Shape):
    @property
    def area(self):
        return self.side ** 2
    
    @property
    def perimeter(self):
        return self.side * 4
    