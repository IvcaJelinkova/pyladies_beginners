from tkinter import N
from turtle import forward, right, left, penup, pendown, exitonclick, speed
import math

speed(10)
left(180)
penup()
forward(350)
right(180)
pendown()

# triangle: 
for i in range(3): 
    forward(40)
    left(120)

penup()
forward(80)
pendown()


# house --> village: 
side = 30
hypotenuse_of_triangle = math.sqrt(2 * side ** 2)

roof_side = math.sqrt(side ** 2 / 2)

print(round(hypotenuse_of_triangle, 2))
print(round(roof_side, 2))

for count in range(5):
    forward(side)
    left(90+45)
    forward(hypotenuse_of_triangle)
    right(45+90)
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
    forward(20)

penup()
forward(40)
pendown()

# pentagon, hexagon, heptagon, octagon: 
# interior angle of n-gon = 180 * (1-2/n) degrees
# side = 200/n

for number_of_sides in range(5, 9):
    angle = 180 * (1 - 2 / number_of_sides)
    for i in range(number_of_sides): 
        side = 200 / number_of_sides
        forward(side)
        left(180 - angle)
    penup()
    forward(side + 45)
    pendown()





exitonclick()

