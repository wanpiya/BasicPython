import sys
print(sys.version)


import turtle
t=turtle.Pen() #ดึงความสามารถไว้กลับมาใช้ปากกา
t.shape('circle') #แปลงไอคอน

def circle():
    ''' ฟังชั่นสำหรับไว้วาดรูป'''
    for i in range (10):
        t.circle(25)
        t.left(36)

def go(x,y):
    '''ฟังชั่นสำหรับเคลื่อนที่'''
    t.penup()
    t.goto(x,y)
    t.pendown()


go(0,0)
circle()
t.dot(15)
t.right(95)
t.forward(75)