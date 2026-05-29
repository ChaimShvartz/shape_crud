from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from json import dump, load
from shape import Shape

class ShapeManager:
    shape_info = {
    "circle": {"class": Circle, "args": ("radius", )},
    "hexagon": {"class": Hexagon, "args": ("side", )},
    "rectangle": {"class": Rectangle, "args": ("width", "height")},
    "square": {"class": Square, "args": ("side", )},
    "triangle": {"class": Triangle, "args": ("height", "base", "side_a", "side_b", "side_c")}
    }

    def __init__(self, filename:str) -> None:
        self.file = filename
        self.shapes = []
        self.load_from_json()

    @staticmethod
    def is_positive_number(value, type):
        try:
            return type(value) > 0
        except ValueError:
            print("Invalid input, try again\n")
            return False

    @staticmethod
    def get_positive_number(parma:str) -> float:
        is_valid_value = False
        type_to_check = int if parma == 'ID' else float
        while not is_valid_value:
            user_input = input(f"Enter {parma}: ")
            is_valid_value = ShapeManager.is_positive_number(user_input, type_to_check)
        return user_input

    def create_shape(self, shape:str) -> Shape:
        kwargs = {"type": shape}
        for arg in self.shape_info[shape]["args"]:
            kwargs[arg] = self.get_positive_number(arg)
        new_shape = self.shape_info[shape]["class"](**kwargs)
        return new_shape

    def add_shape(self, shape_name:str) -> None:
        new_shape = self.create_shape(shape_name)
        self.shapes.append(new_shape)

    def get_all_shapes(self) -> list[dict]:
        return [shape.to_dict() for shape in self.shapes]

    def update_shape(self, shape:Shape) -> bool:
        updated = False
        args = self.shape_info[shape.type]["args"]
        for arg in args:
            user_input = input(f"Do you want reset {arg}(Y/N): ").strip().upper()
            if user_input == 'Y':
                new_value = self.get_positive_number(arg)
                setattr(shape, arg, new_value)
                print(f"{arg} changed")
                updated = True
        return updated
                
    def delete_shape(self, shape:Shape) -> None:
        self.shapes.remove(shape)
        
    def save_to_json(self) -> None:
        with open(self.file, 'w', encoding='utf-8') as f:
            data = self.get_all_shapes()
            dump(data, f, indent=2)

    def load_from_json(self) -> list:
        try:
            with open(self.file, encoding='utf-8') as f:
                data = load(f)
                for shape in data:
                    shape_class = self.shape_info[shape["type"]]["class"]
                    shape_object = shape_class(**shape)
                    self.shapes.append(shape_object)
                
        except FileNotFoundError:
            pass

    def find_shape_by_id(self, shape_id:str) -> Shape | None:
        for shape in self:
            if str(shape.id) == shape_id:
                return shape
        return None

    def __iter__(self):
        return iter(self.shapes)