import turtle as t
from turtle import Screen

tim = t.Turtle()
tim.shape('circle')
tim.color('red')

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

led = t.Screen()
led.exitonclick()