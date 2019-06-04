"""
指数函数
"""
import numpy as np
import matplotlib.pyplot as plt


def exp_function():
    x = np.arange(-2, 2, 0.1)
    print(x)
    y = np.exp(x)
    print(y)

    plt.plot(x, y)
    # plt.ylim(-0.1, 1.1)  # 指定Y轴的范围
    plt.title('exp_function')
    plt.show()
    pass


if __name__ == '__main__':
    exp_function()
