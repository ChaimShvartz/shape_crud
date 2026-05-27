class Shape:
    def __init__(self, shape_id, shape_type, **kwargs):
        self.id = shape_id
        self.shape_type = shape_type
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