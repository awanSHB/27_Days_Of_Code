import turtle
import pandas

screen = turtle.Screen()
screen.title("U-S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Correct Guess", prompt="What is another states name?").title()
    if answer in all_states:
        guessed_states.append(answer)
        top = turtle.Turtle()
        top.hideturtle()
        top.penup()
        state_data = data[data.state == answer]
        print(state_data)
        top.goto(int(state_data.x), int(state_data.y))
        top.write(answer)

screen.exitonclick()