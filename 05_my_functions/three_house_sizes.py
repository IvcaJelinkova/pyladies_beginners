import math
from turtle import left, right, forward, exitonclick, penup, pendown, shape, speed


shape('turtle') 
speed(20)

# house --> 3 house sizes:
def draw_house(side): 
    """It draws a house given size. """
    hypotenuse_of_triangle = math.sqrt(2 * side ** 2)

    roof_side = math.sqrt(side ** 2 / 2)

    print(round(hypotenuse_of_triangle, 2))
    print(round(roof_side, 2))

    forward(side)
    left(90+45)
    forward(hypotenuse_of_triangle)
    right(90+45)
    forward(side)
    left(90+45)
    forward(roof_side)
    left(90)
    forward(roof_side)
    left(45)
    forward(side)
    left(90+45)
    forward(hypotenuse_of_triangle)
    right(90+45)
    forward(side)
    left(90)

    #grass: 
    forward(20)
    penup()
    forward(40)
    pendown()


draw_house(30)
draw_house(40)
draw_house(80)

exitonclick()