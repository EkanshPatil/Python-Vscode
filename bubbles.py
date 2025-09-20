import random
import turtle
paper = turtle.Screen()
paper.bgcolor("aquamarine")

#variables
colours = ["red","yellow","orange","white","cyan","blue","green","pink","purple"]
colour = random.choice(colours)
colour1 = random.choice(colours)
colour2 = random.choice(colours)
colour3 = random.choice(colours)
x = random.randint(-150,150)
y = random.randint(-150,150)
x1 = random.randint(-150,150)
y1 = random.randint(-150,150)
x2 = random.randint(-150,150)
y2 = random.randint(-150,150)
x3 = random.randint(-150,150)
y3 = random.randint(-150,150)
size = random.randint(10,100)
size1 = random.randint(10,100)
size2 = random.randint(10,100)
size3 = random.randint(10,100)
#pens
pen1 = turtle.Turtle()
pen2 = turtle.Turtle()
pen3 = turtle.Turtle()
pen4 = turtle.Turtle()

#bubbles
pen1.up()
pen1.goto(x,y)
pen1.down()
pen1.fillcolor(colour)
pen1.begin_fill()
pen1.circle(size)
pen1.end_fill()

pen2.up()
pen2.goto(x1,y1)
pen2.down()
pen2.fillcolor(colour1)
pen2.begin_fill()
pen2.circle(size1)
pen2.end_fill()

pen3.up()
pen3.goto(x2,y2)
pen3.down()
pen3.fillcolor(colour2)
pen3.begin_fill()
pen3.circle(size2)
pen3.end_fill()

pen4.up()
pen4.goto(x3,y3)
pen4.down()
pen4.fillcolor(colour3)
pen4.begin_fill()
pen4.circle(size3)
pen4.end_fill()

turtle.done()