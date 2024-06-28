import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_data = data["state"]
guessed_states = []


score = 0
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50", prompt="Enter the name of the State").title()
    if answer_state == "Exit":

        missing_states = []
        for state in states_data:
            if state not in guessed_states:
                missing_states.append(state)

        df = pandas.DataFrame(missing_states)
        df.to_csv("need.csv")
        break


    for state in states_data:
        if answer_state == state:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            score += 1
            states = data[data.state == answer_state]
            t.goto(int(states.x.iloc[0]), int(states.y.iloc[0]))
            t.write(answer_state)
            guessed_states.append(answer_state)
    if score == 50:
        break
        print("You have won")

    df = pandas.DataFrame(guessed_states)
    df_to_csv = ("guessed.csv")




# answer_state.xcor = states["x"]
# print(answer_state.xcor)
# print(states)



