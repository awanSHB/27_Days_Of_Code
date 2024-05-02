from turtle import Screen, Turtle

boy = Turtle()
screen = Screen()

def move_forward():
    boy.forward(10)

def move_backward():
    boy.backward(10)

def move_left():
    new_h = boy.heading() + 10
    boy.setheading(new_h)

def move_right():
    new_h = boy.heading() - 10
    boy.setheading(new_h)

def clear():
    boy.clear()
    boy.penup()
    boy.home()
    boy.pendown()

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()