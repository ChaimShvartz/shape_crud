from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, **kwargs):
        super().__init__(width=side, height=side, **kwargs)
    
    