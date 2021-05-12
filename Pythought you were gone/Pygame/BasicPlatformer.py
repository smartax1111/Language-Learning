
import turtle
import os

wn = turtle.Screen()
wn.title("Basic Platformer")
wn.bgcolor("#87CEEB")
wn.setup(width = 1200, height = 800)

# Character
Character = turtle.Turtle()
Character.speed(0)
Character.shape("square")
Character.color("#013220")
Character.shapesize()
Character.penup()
Character.goto(-350, 0)
Character.dy = -1.5

#Platform
Platform  = turtle.Turtle()
Platform.speed(0)
Platform.shape("square")
Platform.color("#964B00")
Platform.shapesize(stretch_wid = 19, stretch_len = 120)
Platform.penup()
Platform.goto(-590, -200)

# Character Moving Functions
def move_left():
    x = Character.xcor()
    x += 7
    Character.setx(x)

def move_right():
    x = Character.xcor()
    x -= 7
    Character.setx(x)

def jump():
    y = Character.ycor()
    if y == 0:
        y += 10
        Character.sety(y)
        y += 10
        Character.sety(y)
        y += 10
        Character.sety(y)
        y += 10
        Character.sety(y)
        y += 10
        Character.sety(y)
        y += 10
        Character.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(move_left, "d")
wn.onkeypress(move_right, "a")
wn.onkeypress(jump, "w")

# Main Game Loop
while True:
    wn.update()

    # Gravity
    if Character.ycor() > 0:
        Character.sety(Character.ycor()+ Character.dy)

    #Platform Checking
    if Character.ycor() <= Platform.ycor() + 199:
        Character.sety(0)





