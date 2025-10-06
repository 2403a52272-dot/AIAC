def calculate_area(shape, x, y=0):
    """Calculate area for a given shape using cleaner design."""
    def rectangle(x, y): 
        return x * y
    def square(x): 
        return x * x
    def circle(x): 
        return 3.14 * x * x
    shape_functions = {
        "rectangle": lambda: rectangle(x, y),
        "square": lambda: square(x),
        "circle": lambda: circle(x)
    }
    return shape_functions.get(shape.lower(), lambda: "Invalid shape")()
shape = input("Enter shape (rectangle/square/circle): ").lower()
if shape == "rectangle":
    x = float(input("Enter length: "))
    y = float(input("Enter width: "))
    print("Area of rectangle:", calculate_area(shape, x, y))
elif shape == "square":
    x = float(input("Enter side length: "))
    print("Area of square:", calculate_area(shape, x))
elif shape == "circle":
    x = float(input("Enter radius: "))
    print("Area of circle:", calculate_area(shape, x))
else:
    print(calculate_area(shape, 0))