import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(n_rows, n_columns, iterations):
    x_cor = np.linspace(-0.22, -0.219, 1000)
    y_cor = np.linspace(-0.70, -0.699, 1000)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    for i in range(x_len):
        for j in range(y_len):
            c = complex(x_cor[i],y_cor[j])
            z = complex(0, 0)
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
            print((i/x_len)*100,"% completed")

    print(output)
    plt.imshow(output.T, cmap = "hot")
    plt.axis("off")
    plt.show()
mandelbrot(1000,1000,120)