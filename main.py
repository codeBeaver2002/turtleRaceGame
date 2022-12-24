from turtle import Turtle, Screen
from random import *

screen = Screen()
WIDTH, HEIGHT = 500, 400
screen.setup(width=WIDTH, height=HEIGHT)
user_guess = screen.textinput(title="make your bet", prompt="which color do u think will win?: ")
race = True
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for i in range(0,len(colors)):
    newTurtle = Turtle(shape="turtle")
    turtles.append(newTurtle)


for i in range(0, len(turtles)):
    turtles[i].penup()
    turtles[i].color(colors[i])
    y = 100-i*35
    turtles[i].goto(-WIDTH/2 + 20, y)


while race:
    for turtle in turtles:
        turtle.forward(randint(0,10))
        if turtle.xcor() > int(WIDTH/2-20):
            if user_guess == turtle.pencolor():
                print(f"you win, the {turtle.pencolor()} turtle won!!")
            else:
                print(f"you lose, the {turtle.pencolor()} turtle won!!")
            race = False


screen.exitonclick()