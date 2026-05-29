from shape_manager import ShapeManager
from shape import Shape

def show_menu() -> None:
    print("""\n=== SHAPE CRUD ===
    1. Add shape
    2. Show all shapes
    3. Update shape
    4. Delete shape
    5. Exit
          """)

def get_shape_name() -> str:
    not_valid_shape = True
    shapes_list = ShapeManager.shape_info.keys()

    while not_valid_shape:
        shape = input(f"Enter shape's name({'/'.join(shapes_list)}):\n").strip().lower()
        if shape in shapes_list:
            not_valid_shape = False
        else:
            print("Invalid input, try again")
    return shape

def get_shape_by_id(manager:ShapeManager) -> Shape | None:
    shape_id = ShapeManager.get_positive_number("ID")
    shape = manager.find_shape_by_id(shape_id)
    if not shape:
        print(f"Shape with {shape_id} ID not found")
    return shape

def handle_add_shape(manager:ShapeManager) -> None:
    shape_name = get_shape_name()
    manager.add_shape(shape_name)
    manager.save_to_json()
    print("Shape added successfully")

def handle_show_shapes(manager:ShapeManager) -> None:
    shapes = manager.get_all_shapes()
    print("\n--- Shapes list ---\n")
    for shape in shapes:
        for key, value in shape.items():
            print(f"    {key.capitalize()}: {value}")
        print()
    input("Enter to continue...")

def handle_update_shape(manager:ShapeManager) -> None:
    shape = get_shape_by_id(manager)
    if not shape:
        return
    updated = manager.update_shape(shape)
    if updated:
        manager.save_to_json()
        print("Details saved successfully")
    else:
        print("Nothing changed")

def handle_delete_shape(manager:ShapeManager) -> None:
    shape = get_shape_by_id(manager)
    if not shape:
        return
    manager.delete_shape(shape)
    manager.save_to_json()
    print("Shape removed successfully")

def main():
    manager = ShapeManager('shapes.json')
    choice = None
    while choice != '5':
        show_menu()
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                handle_add_shape(manager)
            case '2':
                handle_show_shapes(manager)
            case '3':
                handle_update_shape(manager)
            case '4':
                handle_delete_shape(manager)
            case '5':
                pass
            case _:
                print("Invalid input, try again")

if __name__ == '__main__':
    main()