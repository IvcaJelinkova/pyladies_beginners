from turtle import forward, left, right, exitonclick, penup, pendown, speed

speed(20)
penup()
left(90)
forward(200)
pendown()

# bloom: 
# 18 squares rotated by 20 degrees: 
for square in range(18):
    for side in range(4): 
        forward(35)
        left(90)
    left(20)

right(180)
forward(70)

# leaves: 
#for i in range(5): 
left(100)
number_of_sides = 100
angle = 180 * (1 - 2 / number_of_sides)
for i in range(20): 
    side = 200 / number_of_sides
    forward(side)
    left(180 - angle)
left(90)

number_of_sides = 100
angle = 180 * (1 - 2 / number_of_sides)
for i in range(15): 
    side = 200 / number_of_sides
    forward(side)
    left(180 - angle)
left(45)
forward(50)

right(100)
for i in range(20): 
    side = 200 / number_of_sides
    forward(side)
    right(180 - angle)
right(90)

number_of_sides = 100
angle = 180 * (1 - 2 / number_of_sides)
for i in range(15): 
    side = 200 / number_of_sides
    forward(side)
    right(180 - angle)



exitonclick()