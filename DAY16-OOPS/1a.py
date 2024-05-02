# import another_module
# print(another_module.another_variable)

# from object import class
from turtle import Screen, Turtle
#new object is created from the turtle class and is constructed
tim = Turtle()
print(tim)

tim.shape("turtle")
tim.color("green")
tim.forward(200)
tim.left(200)
tim.forward(200)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()         # limiting my screen to stop when i click on it