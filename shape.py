class Shape:
    next_id = 1
    def __init__(self, type, id=None, **kwargs):
        if id is None:
            self.id = Shape.next_id
        else:
            self.id = id
        Shape.next_id = self.id + 1
        self.type = type
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError

    def to_dict(self):
        return self.__dict__
    