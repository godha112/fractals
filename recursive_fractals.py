from turtle import *

def koch_flake(length, order):
    if(order == 0):
        forward(length)
        return
    koch_flake(length/3,order-1)
    left(60)
    koch_flake(length/3, order - 1)
    right(120)
    koch_flake(length/3, order - 1)
    left(60)
    koch_flake(length/3,order-1)
def draw_flake():
    speed(0)
    up()
    backward(200 / 2.0)
    down()
    col = ["red", "green", "blue", "yellow"]
    fillcolor("black")
    begin_fill()
    for i in range(3):
        color(col[i])
        koch_flake(300.0, 4)
        left(-120)
    end_fill()
    mainloop()
def quadrative_koch(length,order):
    angle = 90
    if(order==0):
        forward(length)
        return
    quadrative_koch(length,order-1)
    left(angle)
    quadrative_koch(length,order-1)
    right(angle)
    quadrative_koch(length, order - 1)
    right(angle)
    quadrative_koch(length, order - 1)
    quadrative_koch(length, order - 1)
    quadrative_koch(length, order - 1)
    left(angle)
    quadrative_koch(length, order - 1)
    left(angle)
    quadrative_koch(length, order - 1)
    right(angle)
    quadrative_koch(length, order - 1)
def draw_quadratic_koch():
    speed(0)
    up()
    backward(200.0/2.0)
    down()
    col = ['red', 'blue', 'green', 'yellow']
    for i in range(4):
        color(col[i])
        quadrative_koch(8,2)
        left(90)
    mainloop()
def quadratic_flake(length,order):
    if(order==0):
        forward(length)
        return
    color('red')
    quadratic_flake(length,order-1)
    left(90)
    color('orange')
    quadratic_flake(length, order - 1)
    right(90)
    color('yellow')
    quadratic_flake(length, order - 1)
    right(90)
    color('yellow')
    quadratic_flake(length, order - 1)
    left(90)
    color('black')
    quadratic_flake(length, order - 1)
def draw_quad_flake():
    speed(0)
    up()
    backward(300/2.0)
    down()
    for i in range(2):
        quadratic_flake(6, 4)
        right(180)
    mainloop()

def levy_c_curve(length,order):
    if(order==0):
        forward(length)
        return
    right(45)
    levy_c_curve(length,order-1)
    left(90)
    levy_c_curve(length, order - 1)
    right(45)
def draw_levy_c():
    speed(0)
    up()
    backward(300/2.0)
    down()
    for i in range(2):
        levy_c_curve(8,10)
        right(180)
    mainloop()

def rings(length,order):
    if(order==0):
        forward(length)
        return
    rings(length, order - 1)
    rings(length, order - 1)
    right(90)
    rings(length, order - 1)
    right(90)
    rings(length, order - 1)
    right(90)
    rings(length, order - 1)
    right(90)
    rings(length, order - 1)
    right(90)
    rings(length, order - 1)
    left(90)
    rings(length, order - 1)

def draw_rings():
    speed(0)
    up()
    backward(300.0/2.0)
    down()
    for i in range(4):
        rings(8, 2)
        left(90)
    mainloop()
def pentaplexity(length,order):
    if(order==0):
        forward(length)
        return
    pentaplexity(length,order-1)
    right(36)
    right(36)
    pentaplexity(length, order - 1)
    right(72)
    pentaplexity(length, order - 1)
    right(180)
    pentaplexity(length, order - 1)
    left(36)
    pentaplexity(length, order - 1)
    right(72)
    pentaplexity(length, order - 1)
def draw_pentaplexity():
    speed(0)
    up()
    backward(300.0/2.0)
    left(90)
    down()
    for i in range(5):
        pentaplexity(8, 3)
        right(72)
        pentaplexity(8, 3)
        right(72)
        pentaplexity(8, 3)
        right(72)
        pentaplexity(8, 3)
        right(72)
        pentaplexity(8, 3)
        left(72)
    mainloop()
#draw_flake()
#draw_quadratic_koch()
#draw_quad_flake()
draw_levy_c()
#draw_rings()
#draw_pentaplexity()