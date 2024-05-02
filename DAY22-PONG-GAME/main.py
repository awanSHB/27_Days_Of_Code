'''
1-Create a screen

2-Create a moving paddle

3-Create a paddle class for another paddle

4-Create a ball and make it move

5-Detect collision with ball and mouse

6-Detect collision with paddle

7-Detect when paddle misses

8-detect Score
'''

# 1-Creating the Screen
from turtle import Turtle, title
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('PonG')
screen.tracer(0)
scoreboard = Scoreboard()

# 2-Create and move the paddle
paddle1 = Turtle()
paddle1.color('white')
paddle1.shape('square')
paddle1.shapesize(6, 1)
paddle1.penup()
paddle1.goto(380,0)

def upp():
    new_y = paddle1.ycor() + 80
    paddle1.goto(paddle1.xcor(), new_y)

def downn():
    new_y = paddle1.ycor() - 80
    paddle1.goto(paddle1.xcor(), new_y)

screen.listen()
screen.onkey(upp, 'Up')
screen.onkey(downn, 'Down')

# 3:- Another paddle
paddle2 = Paddle()
screen.onkey(paddle2.go_up, 'w')
screen.onkey(paddle2.go_down, 's')

# 4:- Creating the ball and making it move
ball = Ball()
ball.speed('fast')

# 5:- Bouncing the ball

game_is_on = True
while(game_is_on):
    time.sleep(0.03)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_Y()
    
    #6:- Detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 340 or ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.bounce_X()

    #7:= Detect when the ball misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -440:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()