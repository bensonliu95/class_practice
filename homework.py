from turtle import * 
import random
t=Turtle()
x=random.randint(1,200)
y=random.randint(1,250)
cl=["green","yellow","red","blue","purle"]
shape=["circle","square","triangle"]
t.up()
t.goto(x,y)
t.down()
t.begin_fill
t.random.choice(cl[])
