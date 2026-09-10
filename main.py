import turtle

screen = turtle.Screen()
screen.title("U.S. States Games")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

#to get co-ordinates
#def get_mouse_click_coor(x, y):
 #   print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)

answer_state = screen.textinput(title="Guess the state", prompt="Whats another state name ")
print(answer_state)

import pandas


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()



# ---- TRACK PROGRESS ----
guessed_states = []

# ---- MAIN GAME LOOP ----
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None:
        # Player pressed Cancel — stop the game
        break

    answer_state = answer_state.title()  # fixes capitalization, e.g. "texas" -> "Texas"

    if answer_state == "Exit":
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Find this state's row in the CSV
        state_data = data[data.state == answer_state]

        # Create a turtle just to write text (invisible, no drawing)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# ---- AFTER THE LOOP: FIND MISSED STATES ----
missing_states = [state for state in all_states if state not in guessed_states]

# ---- SAVE MISSED STATES TO A NEW CSV ----
new_data = pandas.DataFrame({"state": missing_states})
new_data.to_csv("states_to_learn.csv")




turtle.mainloop()

