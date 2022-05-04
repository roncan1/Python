import random
import turtle
turtle.title("터틀")
turtle.pensize(3)
turtle.speed(0)
turtle.bgcolor("skyblue")
turtle.shape("turtle")
turtle.colormode(255)
a = int(input("반복"))
c = int(input("도형"))
color = 255
for i in range(a):
    color -= color//a
    turtle.pencolor(100,100,color)
    turtle.circle(80, steps=c)
    turtle.right(360/a)
turtle.mainloop()