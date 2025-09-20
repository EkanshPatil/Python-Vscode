import turtle

pen1 = turtle.Turtle()
pen2 = turtle.Turtle()

pen1.shape("turtle")
pen1.color("green")

pen2.color("black")

paper = turtle.Screen()
pen2.write("begin",font=("Epunda Slab",13,"italic"),align="center")

steps = int(input("How many steps should the turtle move?  "))

def go_forward():
    pen1.forward(steps)

def go_up():
    pen1.setheading(90)

def go_down():
    pen1.setheading(270)        

def go_left():
    pen1.setheading(180)

def go_right():
    pen1.setheading(0)

paper.listen()

paper.onkey(go_forward,"space")
paper.onkey(go_up,"w")
paper.onkey(go_down,"s")
paper.onkey(go_left,"a")
paper.onkey(go_right,"d")

def click(x,y):
    paper.tracer(0)
    pen1.setheading(pen1.towards(x,y))
    pen1.goto(x,y)
    paper.tracer(1)

def drag(x,y):
    paper.tracer(0)
    pen1.goto(x,y)
    paper.tracer(1)

paper.onclick(click)
pen1.ondrag(drag)
turtle.done()
