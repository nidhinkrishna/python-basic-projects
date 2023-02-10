from turtle import Turtle
import random
import turtle
turtle.colormode(255)


dots= Turtle()
dots.speed(0)
dots.penup()
colors=[ (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
         (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10),  (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
         (224, 141, 211), (10, 97, 61)]

dots.setheading(225)
dots.forward(300)
dots.setheading(0)
number_of_dots=101
for dot_count in range(1,number_of_dots) :
    dots.dot(20,random.choice(colors))
    dots.forward(50)

    if dot_count%10==0:
        dots.setheading(90)
        dots.forward(50)
        dots.setheading(180)
        dots.forward(500)
        dots.setheading(0)

dots.hideturtle()
s=turtle.Screen()
s.exitonclick()