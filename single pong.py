import turtle
import winsound
from typing import Set #to access the python library to get shapes
import sys

WIDTH = 800
HEIGHT = 600

wn= turtle.Screen() #to create a screen(seperate window to check your program)
turtle.title("pong by timi") #to give the screen a name
wn.bgcolor("black")     #for the screen color
wn.setup(width=WIDTH, height=HEIGHT)       #for the screen size
wn.tracer(0)    #to reduce lagging due to update and to prevent the sreen from updating    

# score board
HEALTH = 5  #the value for the health(score board)


#paddle

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 100
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 100
    paddle_a.sety(y)

# key binding
wn.listen()
wn.onkeypress(paddle_a_up, "Up")
wn.onkeypress(paddle_a_down, "Down")



#Ball

Ball= turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("red")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.5
Ball.dy = 0.5   

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("HEALTH(5)", align="center", font=("courier", 24, "normal"))


        # Main game loop 
while True:
    wn.update()     
#Ball movement
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)



    # border 
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound ("Various-13.wav", winsound.SND_ASYNC)
        

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        winsound.PlaySound("Various-13.wav", winsound.SND_ASYNC)
    if Ball.xcor() > 390:
        # Ball.goto(0, 0)
        Ball.dx *= -1
        winsound.PlaySound("Various-13.wav", winsound.SND_ASYNC)
    if Ball.xcor() < -390:
        # Ball.goto(0, 0)
        Ball.dx *= -1
        HEALTH -= 1
        if HEALTH < 1:
            pen.clear()
            pen.goto(0, 0)
            pen.write("GAME OVER",  align="center", font=("courier", 50, "normal"))
        else:
            pen.clear()
            pen.write("HEALTH:({})".format(HEALTH), align="center", font=("courier", 24, "normal"))
        
        #border for paddle
    if paddle_a.ycor() > 290:   
         paddle_a.sety(290)     

    if paddle_a.ycor() < -290: 
        paddle_a.sety(-290)     
    # collisions
    if (Ball.xcor() > 350 and Ball.xcor() <350):
        Ball.setx(340)
        Ball.dx *= -1
        winsound.PlaySound("Various-13.wav", winsound.SND_ASYNC)

    if (Ball.xcor() < -340 and Ball.xcor() < -350) and (Ball.ycor() < paddle_a.ycor() + 40 and Ball.ycor() > paddle_a.ycor() -40):
        Ball.setx(-340)
        Ball.dx *= -1
        winsound.PlaySound("Various-13.wav", winsound.SND_ASYNC)






