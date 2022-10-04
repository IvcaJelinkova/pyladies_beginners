from turtle import forward, penup, pendown, exitonclick, right, left

penup()
left(180)
forward(300)
right(180)
pendown()


# dashed line: 
forward(30)
penup()
forward(5)
pendown()
forward(30)


penup()
forward(100)
pendown()



# square: 
for i in range(4): 
    forward(50)
    left(90)

penup()
forward(150)
pendown()



# rectangle: 
for i in range(2): 
    forward(50)
    left(90)
    forward(20)
    left(90)

exitonclick()
