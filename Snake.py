import turtle
import random
import time

paper = turtle.Screen()
paper.bgcolor("aquamarine")

segments = []
score = 0

snake = turtle.Turtle()
snake.color("orange")
snake.shape("square")
snake.penup()
snake.goto(25,50)

food = turtle.Turtle()
food.color("blue")
food.penup()
food.goto(50,100)
food.shape("circle") 

pen = turtle.Turtle()
pen.penup()
pen.goto(0,150)
pen.hideturtle()
pen.write("score= ",str(score),align = "center",font = ("Arial",15,"bold"))

def move():
    if snake.setheading == "Up":
        y = snake.ycor()
        snake.sety(y+7)
    
    if snake.setheading == "Right":
        x = snake.xcor()
        snake.setx(x+7)

    if snake.setheading == "Left":
        x = snake.xcor()
        snake.setx(x-7)

    if snake.setheading == "Down":
        y = snake.ycor()
        snake.sety(y-7)       

def go_up():
    snake.setheading = "Up"

def go_down():
    snake.setheading = "Down"

def go_left():
    snake.setheading = "Left"

def go_right():
    snake.setheading = "Right"    

paper.listen()

paper.onkey(go_up,"w")
paper.onkey(go_down,"s")
paper.onkey(go_right,"d")
paper.onkey(go_left,"a")

while True:
    paper.update()
    move()
    if snake.distance(food)<20:
        x = random.randint(-180,180)
        y = random.randint(-180,180)
        food.penup()
        food.goto(x,y)
        food.pendown()
        score += 1

turtle.done()