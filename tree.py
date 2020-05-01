from turtle import *
def tree(length,angle):
    if(length<9):
        return
    else:
        pencolor('green')
        forward(length)
        right(angle)
        tree(0.8*length,angle)
        left(2*angle)
        tree(0.8*length,angle)
        right(angle)
        backward(length)
        pencolor('brown')
def draw_fractal():
    speed(300)
    up()
    left(90)
    backward(200.0)
    down()
    tree(100,30)
    mainloop()
draw_fractal()