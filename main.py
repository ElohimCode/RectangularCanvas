from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])


def get_color():
    red, green, blue = int(input("How much red? ")), \
                       int(input("How much blue? ")), \
                       int(input("How much green? "))

    return red, green, blue


while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")
    # Ask for rectangle data and create if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rectangle_x = int(input("Enter x of the rectangle: "))
        rectangle_y = int(input("Enter y of the rectangle: "))
        rectangle_width = int(input("Enter the width of the rectangle: "))
        rectangle_height = int(input("Enter the height of the rectangle: "))
        color = get_color()

        # Create the rectangle
        rectangle = Rectangle(x=rectangle_x, y=rectangle_y, height=rectangle_height,
                              width=rectangle_height, color=color)
        rectangle.draw(canvas)

    # Ask for square data and create if user entered 'square'
    if shape_type.lower() == "square":
        square_x = int(input("Enter x of the square: "))
        square_y = int(input("Enter y of the square: "))
        square_side = int(input("Enter the side length of the square: "))
        color = get_color()

        # Create the square
        square = Square(x=square_x, y=square_y, side=square_side, color=color)
        square.draw(canvas)

    if shape_type == 'quit':
        break

canvas.make('canvas.png')
