from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base, **kwargs):
        super().__init__(width=base, **kwargs)

    @property
    def area(self):
        return super().area / 2
    
    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c