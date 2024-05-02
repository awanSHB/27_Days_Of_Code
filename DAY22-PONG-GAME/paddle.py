# 3-Create a paddle class for another paddle

from turtle import Turtle

class Paddle(Turtle):       # This is inherited from the Turtle class
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(6, 1)
        self.penup()
        self.goto(-389,0)

    def go_up(self):
        new_y = self.ycor() + 80
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 80
        self.goto(self.xcor(), new_y)