
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

# Platform 1
Platform1  = turtle.Turtle()
Platform1.speed(0)
Platform1.shape("square")
Platform1.color("#964B00")
Platform1.shapesize(stretch_wid = 19, stretch_len = 120)
Platform1.penup()
Platform1.goto(-590, -200)

# Platform 2
Platform2 = turtle.Turtle()
Platform2.speed(0)
Platform2.shape("square")
Platform2.color("#964B00")
Platform2.shapesize(3, 50)
Platform2.penup()
Platform2.goto(300, 20)

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
    if Character.ycor() <= Platform1.ycor() + 199:
        Character.sety(0)
    if Character.xcor() >= Platform2.xcor() - 512 and Character.ycor() <= Platform2.ycor():
        Character.setx(-210)
    if Character.ycor() <= Platform2.ycor() + 60 and Character.xcor() > -210:
        Character.sety(60)