from turtle import Turtle, Screen

qasim = Turtle()

#Drawing the triangle
qasim.color("blue")
qasim.forward(100)
qasim.right(120)
qasim.forward(100)
qasim.right(120)
qasim.forward(100)
qasim.right(120)

#Drawing the rectangle
qasim.color('black')
qasim.forward(100)
qasim.right(90)
qasim.forward(110)
qasim.right(90)
qasim.forward(100)
qasim.right(90)
qasim.forward(110)
qasim.right(90)

#Drawing the pentagon
qasim.color('red')
qasim.forward(100)
qasim.right(72)
qasim.forward(100)
qasim.right(72)
qasim.forward(100)
qasim.right(72)
qasim.forward(100)
qasim.right(72)
qasim.forward(100)
qasim.right(72)

#Drawing the hexagon
qasim.color('green')
for _ in range(6):
    qasim.forward(100)
    qasim.right(60)

#drawing the heptagon
qasim.color('yellow')
for _ in range(6):
    qasim.forward(100)
    qasim.right(52)
qasim.forward(99)
qasim.right(50)

#Drawing the octagon
qasim.color('brown')
for _ in range(8):
    qasim.forward(100)
    qasim.right(45)

#Drawing the nonagon
qasim.color('magenta')
for _ in range(9):
    qasim.forward(100)
    qasim.right(40)

#Drawing the docagon
qasim.color('purple')
for _ in range(10):
    qasim.forward(100)
    qasim.right(36)
my_s = Screen()
my_s.exitonclick()