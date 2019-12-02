#main program file
from Gaudin1Functions import*

turtle.colormode(255)
bob.width(10)
bob.speed(0)

x = -500
y = 400
jump(x,y)
for times in range(150):
    c = (0,0,65)
    bob.color(c)
    bob.forward(1000)
    jump(x,y-times*6)

jump(0,0)
for times in range(100):
    for c in ("red","blue", "green", "orange"):
        explosion(200,c)
        bob.forward(1)
        bob.right(1)



        



