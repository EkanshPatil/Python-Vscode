import turtle
import random
paper=turtle.Screen()
paper.bgcolor("black")
#variables
colours = ["red","yellow","orange","white","cyan","blue","green","pink","purple"]
x = random.randint(-150,150)
y = random.randint(-150,150)
x1 = random.randint(-150,150)
y1 = random.randint(-150,150)
x2 = random.randint(-150,150)
y2 = random.randint(-150,150)
x3 = random.randint(-150,150)
y3 = random.randint(-150,150)
size = random.randint(1,100)
colour = random.choice(colours)
size1 = random.randint(1,100)
colour1 = random.choice(colours)
size2 = random.randint(1,100)
colour2 = random.choice(colours)
size3 = random.randint(1,100)
colour3 = random.choice(colours)

#pens
pen1 = turtle.Turtle()
pen1.speed(100)
pen1.up()
pen1.goto(x,y)
pen1.color(colour)

pen2 = turtle.Turtle()
pen2.speed(100)
pen2.up()
pen2.goto(x1,y1)
pen2.color(colour1)

pen3 = turtle.Turtle()
pen3.speed(100)
pen3.up()
pen3.goto(x2,y2)
pen3.color(colour2)

pen4 = turtle.Turtle()
pen4.speed(100)
pen4.up()
pen4.goto(x3,y3)
pen4.color(colour3)

#fireworks
for i in range(45):
  pen1.down()
  pen1.forward(size)
  pen1.up()
  pen1.backward(size)
  pen1.right(10)
   
for i in range(45):
  pen2.down()
  pen2.forward(size1)
  pen2.up()
  pen2.backward(size1)
  pen2.right(10)
  
for i in range(45):
  pen3.down()
  pen3.forward(size2)
  pen3.up()
  pen3.backward(size2)
  pen3.right(10)
 
   
for i in range(45):
  pen4.down()
  pen4.forward(size3)
  pen4.up()
  pen4.backward(size3)
  pen4.right(10)   
   
turtle.done()  