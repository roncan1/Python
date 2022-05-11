import turtle as t
t.title("도라에몽")
t.pensize(5)
t.speed(10)
t.penup()
t.goto(-100, -200)
t.pendown()
t.lt(160)
for i in range(115):
    t.fd(4)
    t.rt(1)
    
for i in range(58):
    t.fd(6)
    t.rt(1)

for i in range(35):
    t.fd(4)
    t.rt(1)
    
for i in range(25):
    t.fd(5)
    t.rt(1) 
          
for i in range(35):
    t.fd(4)
    t.rt(1)
    
for i in range(25):
    t.fd(5)
    t.rt(1) 
    
t.rt(39)
t.fd(360)
t.lt(80)
for i in range(2):
    t.lt(5)
    t.fd(13)
t.lt(90)
t.fd(360)
t.lt(80)
for i in range(2):
    t.lt(5)
    t.fd(13)
t.penup()    
t.goto(0, -200)
t.pendown()
t.lt(110)
t.circle(40)
t.penup()    
t.goto(25, -275)
t.pendown()
t.rt(100)
t.fd(30)
t.rt(90)
t.circle(9)
t.penup()    
t.goto(-17, -230)
t.pendown()
t.lt(10)
for i in range(7):
    t.fd(10)
    t.rt(5) 
t.lt(80)
for i in range(2):
    t.lt(5)
    t.fd(3)
t.lt(90)
for i in range(7):
    t.fd(10)
    t.lt(6) 
t.penup()    
t.goto(-217, -100)
t.pendown()
t.rt(100)
for i in range(45):
    t.fd(6)
    t.rt(2)
    
t.rt(90)
for i in range(30):
    t.fd(3)
    t.lt(3)
    
t.rt(100)
t.circle(30)
t.mainloop()