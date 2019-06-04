import numpy as np

"""
均方误差测试
"""


def mean_squared_error_1(y, t):
    sum = 0
    for x in range(len(y)):
        # print(y[x], t[x], (y[x] - t[x]) ** 2)
        sum = sum + (y[x] - t[x]) ** 2
    return sum / 2


def mean_squared_error_2(param, param1):
    x = param - param1
    xx = x ** 2
    sum = np.sum(xx)
    # print(x)
    # print(xx)
    # print(sum)
    return sum * 0.5
    pass


if __name__ == '__main__':
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    print(t, y)
    mean1 = mean_squared_error_1(y, t)
    print(mean1)
    mean2 = mean_squared_error_2(np.array(y), np.array(t))
    print(mean2)

    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    mean2 = mean_squared_error_2(np.array(y), np.array(t))
    print(mean2)

    pass
