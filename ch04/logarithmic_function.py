import numpy as np
import matplotlib.pyplot as plt

"""
对数函数
"""


def log_function():
    x = np.arange(0.01, 1.1, 0.01)
    print(x)
    y = np.log2(x)
    print(y)

    plt.plot(x, y)
    # plt.ylim(-0.1, 1.1)  # 指定Y轴的范围
    plt.title('log_function')
    plt.show()
    pass

    pass


if __name__ == '__main__':
    log_function()
