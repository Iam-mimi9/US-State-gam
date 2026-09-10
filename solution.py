import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. state game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
#if answer state is correct
all_states = data.state.to_list()
guessed_states =[]

while len(guessed_states) < 50:
   answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt="Guess another the state").title()

   if answer_state  == "Exit":
      missing_states = [state for state in all_states if state not in guessed_states]
      #for state in all_states:
       #  if state not in guessed_states:
        #     missing_states.append(state)
      new_data = pandas.DataFrame(missing_states)
      new_data.to_csv("missing_states.csv")
      break



   # if answer state is one of  the states in all states
   if answer_state in all_states:
      guessed_states.append(answer_state)
      # create a turtle to write the name of the state at the state x and y coordinates
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = data[data.state == answer_state]
      t.goto(state_data.x.item(), state_data.y.item())
      t.write(answer_state)




