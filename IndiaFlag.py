import turtle
 
pen=turtle.Turtle()
paper=turtle.Screen()

pen.pencolor("black")

#green
pen.up()
pen.goto(-100,-50)
pen.down()
pen.fillcolor("green")
pen.begin_fill()
pen.forward(200)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(50)
pen.end_fill()

#white
pen.left(180)
pen.forward(100)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(50)

#orange
pen.left(180)
pen.forward(50)
pen.fillcolor("orange")
pen.begin_fill()
pen.forward(50)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(50)
pen.end_fill()

#chakra
pen.pencolor("blue")
pen.up()
pen.goto(-25,25)
pen.down()
pen.circle(25)
pen.up()
pen.goto(0,25)
pen.down()
for i in range (15):
  pen.forward(25)
  pen.left(180)
  pen.forward(25)
  pen.left(204)

#pole
pen.up()
pen.goto(-100,-50)
pen.down()
pen.pencolor("black")
pen.forward(100)
pen.left(90)
pen.forward(15)
pen.left(90)
pen.forward(100)
