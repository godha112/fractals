import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(n_rows, n_columns, iterations, cx, cy):
    x_cor = np.linspace(-2, 2, n_rows)
    y_cor = np.linspace(-2, 2, n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    c = complex(cx, cy)
    for i in range(x_len):
        for j in range(y_len):
            z = complex(x_cor[i], y_cor[j])
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
        print(int((i/x_len)*100),"% completed")

    print(output)
    plt.imshow(output.T, cmap='hot')
    plt.axis("off")
    plt.show()
CX = float(input("enter the value of cx - "))
CY = float(input("enter the value of cy - "))
nrow = int(input("enter the number of rows - "))
ncolumn = int(input("enter the number of columns - "))
steps = int(input("enter the number of iterations - "))
mandelbrot(nrow,ncolumn,steps,CX,CY)
