import turtle
 
pen=turtle.Turtle()
paper=turtle.Screen()

pen_colour = input("what should the pen colour be?")
pen.pencolor(pen_colour)

bg_colour = input("what should the background colour be?")
paper.bgcolor(bg_colour)

#diamond
pen.up()
pen.goto(-175,0)
pen.down()
diamond_colour = input("what should the colour of the first shape be?")
pen.fillcolor(diamond_colour)
pen.begin_fill()
pen.left(60)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(60)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.end_fill()

#triangle
pen.up()
pen.goto(0,-175)
triangle_fill = input("what should the colour of the second shape be?")
pen.fillcolor(triangle_fill)
pen.begin_fill()
pen.down()
pen.left(60)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.end_fill()

#octogan
pen.up()
octogan_colour = input("what should the colour of the third shape be?")
pen.fillcolor(octogan_colour)
pen.begin_fill()
pen.goto(100,0)
pen.down()
pen.right(120)
for i in range(8):
 pen.forward(75)
 pen.right(45)
pen.end_fill() 