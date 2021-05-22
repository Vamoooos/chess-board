import turtle as t

t.speed(0)
t.pensize(4)
t.penup()
t.goto(-200, -200)
t.pendown()
a=0
b=0
for i in range(1,9):  #위로 올라감 1,2,3,4,5,6,7,8
    if (b==0):
        a=1
    else:
        a=0
    y = -200
    for j in range(8): #가로로 8번
        if (a==0):
            t.fillcolor("white")
            a=1
        elif (a==1):
            t.fillcolor("black")
            a=0
        t.begin_fill()
        for _ in range(4): #사각형 그리는
            t.forward(50)
            t.left(90)
        t.end_fill()
        t.forward(50)
    if(b==0):
        b=1
    else:
        b=0
    t.penup()
    t.goto(-200, y+50*i)
    t.pendown()

t.done()