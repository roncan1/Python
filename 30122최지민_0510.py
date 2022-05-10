import turtle
turtle.title("터틀")
turtle.pensize(3)
turtle.speed(5)
turtle.bgcolor("skyblue")
turtle.shape("turtle")
turtle.colormode(255)
# col = 255
# for i in range(30):
#     col -=255//30
#     turtle.color(col,0,0)
#     turtle.begin_fill()
#     turtle.circle(100, steps=8)
#     turtle.end_fill()
#     turtle.rt(6)

# turtle.mainloop()

turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
col = 255
radius = 300
for i in range(15,2,-1):
    col -= 255//15
    turtle.color(133,col,133)
    radius -= 20
    turtle.begin_fill()
    turtle.circle(radius, steps=i)
    turtle.end_fill()
    
turtle.mainloop()