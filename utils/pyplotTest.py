"""
显示图形
"""

import numpy as np
import matplotlib.pyplot as plt


def show_sin():
    x = np.arange(0, 6, 0.1)
    print(x)
    y = np.sin(x)
    print(y)
    plt.plot(x, y)
    plt.show()


def show_cos():
    x = np.arange(0, 6, 0.1)
    print(x)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label="sin")
    plt.plot(x, y2, linestyle="--", label="sin")
    plt.title('sin & cos')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    pass


if __name__ == '__main__':
    # show_sin()
    show_cos()
