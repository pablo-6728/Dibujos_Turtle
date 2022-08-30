from lib2to3.pytree import convert
from re import X
from stat import UF_OPAQUE
from turtle import *
from  math import *

#dibujo de un cuadrado usando Turtle

#color('#black')
#begin_fill()

#dibujar cuadrado
def drawSquare():
    while True:
        forward(200)
        #se mueve 270 grados con respecto a la direccion que 
        left(90)
        if abs(pos())<1:
            break
#end_fill()

#dibujar un plano cartesiano
def drawPlane():
    up()
    goto(300, 0)
    pendown()
    goto(-300, 0)
    up()
    goto(0,300)
    pendown()
    goto(0,-300)

def drawLine():
    color('red', 'black')
    up()
    goto(-200, -100)
    down()
    goto(200, 100)

def drawCircle():
    color('blue', 'black')
    r = 100
    a = 200
    b = 200
    c = a**2 + b**2 - r**2

    x = 40
    y = sqrt(r**2 - x**2)
    home()
    goto(-r, 0)
    down()

    #for i in r:
     #   y = sqrt(x**2 + a*x + )
      #  goto(x, y)

    #dibujar en el origen
    for x in range(-r, r+1):
        
        if r**2 - x **2 > 0:
            y = sqrt(r**2 - x**2)
            goto(x, y)
            x = x + 1

        else:
            y = sqrt(abs(r**2 - x**2))
            goto(x, -y)
            x = x - 1

    for x in reversed(range(-r, r+1)):
        
        if r**2 - x **2 > 0:
            y = sqrt(r**2 - x**2)
            goto(x, -y)
            x = x + 1
        else:
            y = sqrt(abs(r**2 - x**2))
            goto(x, -y)
            x = x - 1

def drawParabola():
    color('green', 'black')
    x = -25
    #goto(x, -40)
    
    #parabola positiva
    for x in range(-15,15):
        y = x**2
        goto(x, y)
        down()
    
    up()
    #parabola negativa
    color('orange', 'black')
    for x in range(-15,15):
        y = x**2
        goto(x, -y)
        down()

def drawSpiral():
    home()
    color('purple', 'black')
    down()
    for i in range(35):
        forward(20 + i)
        right(30 - i/1.5)


drawPlane()
drawLine()
up()
drawCircle()
up()
drawParabola()
up()
drawSpiral()
#drawSquare()

done()
    