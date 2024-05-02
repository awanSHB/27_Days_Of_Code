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

direction = [0, 90, 180, 270]
jim.pensize(15)
jim.shape('turtle')
jim.speed('fastest')

for _ in range(200):
    jim.color(random_colors())
    jim.forward(30)
    jim.setheading(random.choice(direction))


lep = t.Screen()
lep.exitonclick()