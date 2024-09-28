#Make a US State Quiz Game
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
#find the state on the list in the CSV file
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    #Using a turtle box that says "What's another state's name?"
    #and a scoreboard ex. X/50 States Correct
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    #test
    #print(answer_state)
    if answer_state == "Exit":
        #creating a list of states the user didn't learn
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle
        t.penup()
        state_data = data[data.state == answer_state]
        #Get the X, Y coordinates from the CSV file
        t.goto(int(state_data.x), int(state_data.y))
        #Print the state name onto the map using the X, Y coordinates
        #.item() gets the first item in a list in pandas
        t.write(state_data.state.item()) # write the name








