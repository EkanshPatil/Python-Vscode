import turtle


pen1 = turtle.Turtle()
pen1.up()
pen1.goto(-150,150)
pen1.color("goldenrod","purple")
pen1.down()

pen2 = turtle.Turtle()
pen2.up()
pen2.goto(150,150)
pen2.color("turquoise","firebrick")
pen2.down()

pen3 = turtle.Turtle()
pen3.up()
pen3.goto(150,-150)
pen3.color("MediumAquamarine","chocolate")
pen3.down()

pen4 = turtle.Turtle()
pen4.up()
pen4.goto(-150,-150)
pen4.color("chartreuse","VioletRed")
pen4.down()

squares = [pen1,pen2,pen3,pen4]

pen1.speed(10)
pen2.speed(10)
pen3.speed(10)
pen4.speed(10)

def square(pen):
  pen.begin_fill()
  for i in range(4):
    pen.forward(70)
    pen.right(90)
  pen.end_fill()

for j in range(36):
  for i in squares:
    square(i)
    i.right(10)

turtle.done()