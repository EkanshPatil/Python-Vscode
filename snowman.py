import turtle

pen=turtle.Turtle()
paper=turtle.Screen()
pen.pensize(5)
pen.pencolor("black")

colour = input("What should the background colour be? ")
paper.bgcolor(colour)

pen.fillcolor("white")
pen.begin_fill()

pen.circle(50) #head

body = 0 #body
while body < 36 :
 pen.forward(15)
 pen.right(10)
 body = body + 1
pen.end_fill()

 
pen.up()
pen.goto(-20,60) #left-eye
pen.down()
pen.circle(5)

pen.up()   #right-eye
pen.goto(20,60) 
pen.down()
pen.circle(5)

pen.up()
pen.goto(-20,30)
pen.down()
pen.right(90)

smile = 0 #smile
while smile < 18 :
 pen.left(10)
 pen.forward(3.5)
 smile = smile + 1
  
pen.up()
pen.goto(7,-30)
pen.down()
pen.fillcolor("black") #first-button
pen.begin_fill()
pen.circle(7)
pen.end_fill()

pen.up()
pen.goto(7,-75)
pen.down()
pen.fillcolor("black") #second-button
pen.begin_fill()
pen.circle(7)
pen.end_fill()

pen.up()
pen.goto(7,-125)
pen.down()
pen.fillcolor("black") #third-button
pen.begin_fill()
pen.circle(7)
pen.end_fill()


pen.up()
pen.goto(-20,100)
pen.down()

hat_colour = input("What should the colour of the hat be? ") #hat
pen.fillcolor(hat_colour)
pen.begin_fill()
hat = 0 
while hat < 20:
 pen.right(10)
 pen.forward(5)
 hat = hat + 1
pen.end_fill()

pen.up()

pen.goto(5,130)  #pom-pom
pen.down()       
pen.fillcolor("white")
pen.begin_fill() 
pen.circle(15)
pen.end_fill()

pen.up()
pen.goto(-75,-50) 
pen.right(110) #left-arm
pen.down()
pen.pencolor("brown")
pen.forward(50)

pen.up()
pen.goto(80,-50) #right-arm
pen.left(270)
pen.down()
pen.forward(50)

pen.hideturtle()