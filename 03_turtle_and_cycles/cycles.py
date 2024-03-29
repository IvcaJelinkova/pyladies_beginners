from turtle import forward, left, right, penup, pendown, exitonclick


for salute in 'Ahoj', 'Hello', 'Hola', 'Hei', 'SYN':
	print(salute + '!')


# dashed line: _ _ _ _ 
for _ in range(15): 
	forward(2 * _)
	penup()
	forward(5)
	pendown()

penup()
right(90)
forward(90)
right(90)
forward(500)
left(180)
pendown()


# three squares rotated by 20 degrees: 
for _ in range(3): 
	for i in range(4): 
		forward(40)
		left(90)
	left(20)


penup()
forward(150)
right(60)
pendown()



# stairs: 
for _ in range(6): 
	forward(30)
	left(90)
	forward(30)
	right(90)


penup()
forward(150)
right(60)
pendown()



# hexagon 6times / flower:  
for i in range(6): 
	for i in range(6): 
		forward(30)
		right(60)

	right(120)
	forward(30)
	left(60)

exitonclick()


