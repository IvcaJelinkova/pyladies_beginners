from tkinter import N
from turtle import forward, right, left, penup, pendown, exitonclick, speed
import math

speed(20)

left(180)
penup()
forward(350)
right(90)
forward(200)
right(90)
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



# ___
penup()
right(175)
forward(600)
pendown()


# regular n-gon, n from the user: 
while True: 
    number_of_sides = input('How many sides would have your n-gon? ')

    try: 
        number_of_sides = int(number_of_sides)
    except ValueError: 
        print('Toto není číslo! ')
    else: 
         if number_of_sides == 0: 
            print('Nula stran neumím... ')
            continue
         angle = 180 * (1 - 2 / number_of_sides)
         for i in range(number_of_sides): 
            side = 200 / number_of_sides
            forward(side)
            left(180 - angle)
         break
        
# ___
penup()
left(140)
forward(120)
pendown()



# regular 100-gon: 
number_of_sides = 100
angle = 180 * (1 - 2 / number_of_sides)
for i in range(number_of_sides): 
    side = 200 / number_of_sides
    forward(side)
    left(180 - angle)

penup()
left(40)
forward(180)
pendown()


# angular spiral: 
for i in range(40): 
    left(90)
    forward(2 * i)


# ___
penup()
right(150)
forward(350)
pendown()


# even more angular spiral too: 
side = 5
for i in range(50): 
    left(45)
    forward(side)
    side += 2


#____
penup()
left(70)
forward(350)
pendown()



# spiral: 
angle = 10
side = 0.05
for i in range(1,400): 
    forward(side)
    left(angle)
    side += 0.05



# ____
penup()
forward(200)
pendown()


# 18 squares rotated by 20 degrees: 
for square in range(18):
    for side in range(4): 
        forward(15)
        left(90)
    left(20)
    

    

exitonclick()

