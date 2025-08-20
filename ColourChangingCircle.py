import turtle

pen = turtle.Turtle()


while True :
  color = input("what should the colour of the circle be?")
  pen.fillcolor(color)
  pen.begin_fill()
  pen.circle(50)
  pen.end_fill()
