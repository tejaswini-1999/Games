from turtle import Turtle, Screen
import random

screen = Screen()

# setting window size - width = 400 and height = 500
screen.setup(600, 400)

user_input = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Choose a color: ")

# Creating objects for each turtle
red = Turtle()
blue = Turtle()
yellow = Turtle()
coral = Turtle()
green = Turtle()
end_line = Turtle()

turtles = [red, blue, yellow, coral, green]

for t in turtles:
   t.hideturtle()

# Setting up the finishing line
end_line.hideturtle()
end_line.penup()
end_line.setpos(260, 150)
end_line.pendown()
end_line.right(90)
end_line.forward(300)

# Setting shape, position, speed and lifting the pen to avoid drawing
y_cood = 100

colors = ["red", "blue", "yellow", "coral", "green"]

for i in range (len(turtles)):
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].speed(0)
    turtles[i].setpos(-280, y_cood)
    turtles[i].showturtle() 
    y_cood -= 50

x_cood = -280

while x_cood <= 260:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if x_cood < t.xcor():
            x_cood = t.xcor()
        
        if x_cood >= 260:
            winner = t.color()[0]
            break   

if user_input != winner:
    print(f"You lose, The {winner} turtle is the winner")
else:
    print("You win!")
   
screen.exitonclick()