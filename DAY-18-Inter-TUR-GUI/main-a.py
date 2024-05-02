#from turtle module import Turtle class
from turtle import Turtle, Screen
import turtle

#Turtle object saved inside the variable
timmy_the_turtle = Turtle()

#changing the shape of the turtle
timmy_the_turtle.shape('turtle')

#changing the color of the turtle
timmy_the_turtle.color("green")

#moving the turtle
timmy_the_turtle.forward(150)

#turning the turtle by degree
timmy_the_turtle.left(90)

timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(150)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(124)
timmy_the_turtle.forward(200)

#printing the screen for the turtel graphics
scrin = Screen()
#screen will close when clocking on it
scrin.exitonclick()