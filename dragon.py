from turtle import *

def dragon_fractal(iterations, axiom, var1, replace1, var2, replace2, length, angle):
    old = axiom
    for i in range(iterations):
        new = ''
        for char in old:
            if(char==var1):
                new += replace1
            elif(char==var2):
                new += replace2
            else:
                new += char
        old = new
    for char in old:
        if(char=="F"):
            forward(length)
        elif(char=='+'):
            right(angle)
        elif(char=='-'):
            left(angle)

def draw_fractal(fractal_name):
    speed(0)
    bgcolor('black')
    pencolor('orange')
    if(fractal_name=="dragon"):
        up()
        backward(200.0 / 2.0)
        left(90)
        down()
        dragon_fractal(10, 'FX', 'X', "X+YF+", "Y", "-FX-Y", 8, 90)
        mainloop()
    elif(fractal_name=="terdragon"):
        up()
        backward(200.0 / 2.0)
        right(180)
        down()
        dragon_fractal(5, "F", "F", "F-F+F", " ", " ", 20, 120)
        mainloop()
    elif(fractal_name=="twin dragon"):
        up()
        backward(200.0 / 2.0)
        left(90)
        down()
        for i in range(3):
            dragon_fractal(9, "FX+FX", "X", "X+YF+", "Y", "-FX-Y", 6, 90)
            right(90)

        mainloop()
    elif(fractal_name=="three dragon"):
        dragon_fractal(10, "FX+FX+FX", "X", "X+YF+", "Y", "-FX-Y", 6, 90)
        mainloop()
    else:
        print("fractal not available!!")

print("following fractals can be drawn : ")
print(" dragon","\n","terdragon","\n","twin dragon","\n","three dragon")
fractal = input("enter the fractal name: ")
draw_fractal(fractal)