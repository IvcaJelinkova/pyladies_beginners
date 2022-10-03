from turtle import forward, penup, pendown, exitonclick, right, left

'''
forward(30)
penup()
forward(5)
pendown()
forward(30)

exitonclick()
'''

# square: 
for i in range(4): 
    forward(50)
    left(90)

right(90)
penup()
forward(60)
left(90)
pendown()


# rectangle: 
for i in range(2): 
    forward(50)
    left(90)
    forward(20)
    left(90)

exitonclick()
