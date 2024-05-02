import turtle as t
import random

jim = t.Turtle()
t.colormode(255)

# generating the rgb colors
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color
jim.speed('fastest')

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        jim.color(random_colors())
        jim.circle(100)
        jim.setheading(jim.heading() + size_of_gap)

spirograph(5)

scr = t.Screen()
scr.exitonclick()