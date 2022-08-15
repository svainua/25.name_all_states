from turtle import Turtle, Screen
import pandas
from print_on_screen import PrintOnScreen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tim = Turtle()
tim.shape(image)

score = 0
correct_answers = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while score < 50:
    answer_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")).title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        location = (int(state_data.x), int(state_data.y))
        print_on_screen = PrintOnScreen(answer_state, location)
        correct_answers.append(answer_state)
        score += 1

states_to_learn = list(set(all_states) ^ set(correct_answers))
states_to_learn_csv = pandas.DataFrame(states_to_learn)
states_to_learn_csv.to_csv("States_to_learn.csv")


     