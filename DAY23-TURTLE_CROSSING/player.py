from turtle import Turtle

Move_Distance = 10
Starting_Position = (0, -280)
Finish_Line = 280

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)
    
    def go_up(self):
        self.forward(Move_Distance)

    def go_to_start(self):
        self.goto(Starting_Position)
    
    def is_at_finish(self):
        if self.ycor() > Finish_Line:
            return True
        else:
            return False