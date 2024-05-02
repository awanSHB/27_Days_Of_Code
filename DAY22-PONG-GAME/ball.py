from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(1, 1)
        self.x = 10
        self.y = 10
        self.penup()
    
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_Y(self):
        self.y*=-1

    def bounce_X(self):
        self.x *= -1
    
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_X()