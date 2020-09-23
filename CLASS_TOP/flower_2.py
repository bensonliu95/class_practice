from turtle import * 

pen = Turtle()
pen.speed(0)
pen.color("red")
for x in range(100):
    pen.circle(x)
    pen.left(90)
done()