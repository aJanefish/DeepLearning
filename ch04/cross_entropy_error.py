"""
交叉熵误差
"""
import numpy as np


def cross_entropy_error(y, t):
    delta = 1e-7
    # print(delta)
    y = y + delta
    # print(y)
    y = np.log(y)
    # print(y)

    result = y * t
    # print(result)
    sum = np.sum(result)
    print(sum)
    return -sum
    pass


if __name__ == '__main__':
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    print(t)
    print(y)

    mean2 = cross_entropy_error(np.array(y), np.array(t))
    print(mean2)

    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
    mean2 = cross_entropy_error(np.array(y), np.array(t))
    print(mean2)
