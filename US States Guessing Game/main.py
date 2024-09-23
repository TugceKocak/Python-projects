import csv
import pandas as pd
import turtle

screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim=turtle.Turtle()
tim.penup()
tim.hideturtle()

# ekrana tıkladığın yerin koordinalarını alma yöntemi

# def get_mouse_click_coordinates(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)
data=pd.read_csv("50_states.csv")
states=data["state"].tolist()

guessed_states=[]
while len(guessed_states)!=50:

    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state=="Exit":
        break
    result = any(answer_state in states for item in states)
    if bool(result):
        guessed_states.append(answer_state)
        x=int(data[data["state"]==answer_state].x.iloc[0])
        y=int(data[data["state"]==answer_state].y.iloc[0])
        tim.goto(x,y)
        tim.write(answer_state, align="center", font=("Arial", 16, "bold"))

#missing states
missing_states=[]
for state in states:
    if state not in guessed_states:
        missing_states.append(state)

missing_dict={"state":missing_states}
pd.DataFrame.from_dict(missing_dict).to_csv("missing_states.csv")

turtle.mainloop()


