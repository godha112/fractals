from turtle import *

def sierpinski(iteration, axiom, rules, length, angle):
    old = axiom
    var1 = rules[0]
    replace1 = rules[1]
    var2 = rules[2]
    replace2 = rules[3]
    for i in range(iteration):
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
        if (char == "F"):
            forward(length)
        elif (char == '+'):
            right(angle)
        elif (char == '-'):
            left(angle)
def draw_fractal(fractal_name):
    speed(0)
    if(fractal_name=="sierpinski-arrowhead"):
        up()
        backward(200.0/2.0)
        left(180)
        down()
        bgcolor("black")
        pencolor("blue")
        sierpinski(7, "YF", ["X", "YF+XF+Y", "Y", "XF-YF-X"], 2, 60)
        mainloop()
    elif(fractal_name=="sierpinski-sieve"):
        up()
        backward(200.0 / 2.0)
        down()
        bgcolor("black")
        pencolor("light green")
        sierpinski(6, "FXF--FF--FF", ["F", "FF", "X", "--FXF++FXF++FXF--"], 2, 60)
        mainloop()

print("select one of these:","\n"," sierpinski-sieve","\n"," sierpinski-arrowhead")

fract = input("enter the fractal name: ")
draw_fractal(fract)
