from turtle import * 

import turtle
t=turtle.Turtle()

cc=["red","blue","green","purple","orange","brown"]
t.speed(0)
for x in range(6):
    t.color(cc[x])
    t.penup()
    t.goto(0,0)
    if x==0:
        t.right(-15)
    else:
        t.right(-30)
    t.pendown()
    t.begin_fill()
    t.circle(150,90)
    t.left(90)
    t.circle(150,90)
    t.end_fill()

done()