import turtle
import pandas
from names import Names

# from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text_box = Names()
# score = ScoreBoard()
game_is_on = True

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name?")

    if answer_state == "Exit":
        missed_states = [state for state in states_list if state not in guessed_states]
        break

    for states in states_list:
        if answer_state.title() == states:
            guessed_states.append(answer_state)
            position_frame = data[data.state == answer_state.title()]
            coord_x = int(position_frame.x)
            coord_y = int(position_frame.y)
            text_box.goto(coord_x, coord_y)
            text_box.write(f"{answer_state.title()}")


df = pandas.DataFrame(missed_states)
df.to_csv("missed_states.csv")

