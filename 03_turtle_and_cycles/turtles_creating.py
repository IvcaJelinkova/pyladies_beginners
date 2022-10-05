from turtle import forward, right, left, penup, pendown, exitonclick
import math

left(180)
penup()
forward(300)
right(180)
pendown()

# triangle: 
for i in range(3): 
    forward(40)
    left(120)

penup()
forward(60)
pendown()


# house --> village: 
side = 30
hypotenuse_of_triangle = math.sqrt(2 * side ** 2)

b_side = math.sqrt(side ** 2 / 2)

print(round(hypotenuse_of_triangle, 2))
print(round(b_side, 2))

for count in range(5):
    forward(side)
    left(90+45)
    forward(hypotenuse_of_triangle)
    right(45+90)
    forward(side)
    left(90+45)
    forward(b_side)
    left(90)
    forward(b_side)
    left(45)
    forward(side)
    left(90+45)
    forward(hypotenuse_of_triangle)
    right(90+45)
    forward(side)
    left(90)
    forward(20)





exitonclick()

