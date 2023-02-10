from turtle import Turtle,Screen
import random
import turtle
turtle.colormode(255)
sp=Turtle()
sp.pensize(3)
sp.speed(0)
def random_color():
    r=random.randint(0,255)
    g= random.randint(0, 255)
    b= random.randint(0, 255)
    rc=(r,g,b)
    return rc
def size_of_gap(size):
    for i in range(int(360/size)):
        sp.color(random_color())
        sp.circle(100)
        sp.setheading(sp.heading()+size)

size_of_gap(10)


sp.hideturtle()
s=Screen()
s.exitonclick()
