import turtle
import random

paper = turtle.Screen()

#racers
pen1 = turtle.Turtle()
pen1.up()
pen1.shape("turtle")
pen1.goto(0,300)


pen2 = turtle.Turtle()
pen2.up()
speed2 = random.randint(1,35)
pen2.color("green")
pen2.shape("turtle")
pen2.goto(0,200)

pen3 = turtle.Turtle()
pen3.up()
speed3 = random.randint(1,35)
pen3.color("orange")
pen3.shape("turtle")
pen3.goto(0,100)

pen4 = turtle.Turtle()
pen4.up()
speed4 = random.randint(1,35)
pen4.color("red")
pen4.shape("turtle")

position1 = pen4.pos()
#commentator
pen5 = turtle.Turtle()
pen5.up()


#user
def go_forward():
    pen1.forward(36)

paper.listen()

paper.onkey(go_forward,"space")

print(position1)
#bots
while True:
    pen2.forward(speed2)
    pen3.forward(speed3)
    pen4.forward(speed4)

if position1 > 99:
  pen5.forward(50)
   
turtle.done()
