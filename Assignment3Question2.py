import math
#triangle
def area_triangle(base,height):
    return 0.5 *base *height
#square
def area_square(side):
    return side * side
#circle
def area_circle(radius):
    return math.pi*radius**2
#rectangle
def area_rectangle(length, width):
    return length * width
print("Triangle area:", area_triangle(10, 5)) 
print("Square area:", area_square(4))
print("Circle area:", area_circle(7))
print("Rectangle area:", area_rectangle(8, 3))