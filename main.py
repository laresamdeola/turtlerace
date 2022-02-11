from turtle import Turtle, Screen
from random import randint


is_race_on = False
race_screen = Screen()
race_screen.screensize(canvwidth=650, canvheight=650)
turtle_choice = race_screen.textinput(title="Race Turtle", prompt="Select a color of the rainbow for your race turtle")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "magenta", "cyan", "brown"]
x_axis = -600
y_axis = [-400, -300, -200, -100, 0, 100, 200, 300, 400, 500]
all_race_turtles = []


for i in range(len(y_axis)):
    new_race_turtle = Turtle()
    new_race_turtle.shape("turtle")
    new_race_turtle.color(turtle_colors[i])
    new_race_turtle.penup()
    new_race_turtle.goto(x=x_axis, y=y_axis[i])
    all_race_turtles.append(new_race_turtle)


if turtle_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_race_turtles:
        if turtle.xcor() > 580:
            is_race_on = False
            winning_turtle = turtle.fillcolor()
            if winning_turtle == turtle_choice:
                print(f"You have won the race with {winning_turtle} turtle")
            else:
                print(f"You have lost the race to {winning_turtle} turtle")
        random_pace = randint(0, len(turtle_colors))
        turtle.forward(random_pace)


race_screen.listen()
race_screen.exitonclick()