import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coor(x,y):
    print(x, y)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# for getting the coordinats of states
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#
# screen.exitonclick()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct", prompt="Enter the state:").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        guessed_states.append(answer_state)
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()