import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")

image = r"C:\Users\jenia\Desktop\learn_python\day_21\us-states-game\blank_states_img.gif"

turtle.addshape(image)
turtle.shape(image)
guessed_states = []
data = pandas.read_csv(r"C:\Users\jenia\Desktop\learn_python\day_21\us-states-game\50_states.csv")
states = data.state.to_list()


while len(guessed_states) < 50:
    state = turtle.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state name?").title()
    if state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        ungessed_df = pandas.DataFrame(missing_states)
        ungessed_df.to_csv(r"C:\Users\jenia\Desktop\learn_python\day_21\us-states-game\ungessed_states.csv")
        break
    if state in states and state not in guessed_states:
        guessed_states.append(state)
        
        t = turtle.Turtle()
        
        t.penup()
        t.hideturtle()
        state_data = data[data.state == state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item(), align="left", font=("Arial", 10, "normal"))
        
