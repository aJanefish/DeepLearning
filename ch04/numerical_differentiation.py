"""
数值微分
"""
import numpy as np
import matplotlib.pyplot as plt


def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x


def function_2(x):
    return 0.2 * x - 0.25


def function_3(x):
    return 0.3 * x - 1


def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def numerical_differentiation():
    x = np.arange(0, 20, 0.01)
    y = function_1(x)

    y2 = function_2(x)
    y3 = function_3(x)

    plt.plot(x, y)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.xlabel("x")
    plt.ylabel("f(x) = 0.01 * x ** 2 + 0.1 * x")
    plt.show()
    pass


if __name__ == '__main__':
    #
    dx5 = numerical_diff(function_1, 5)
    dx10 = numerical_diff(function_1, 10)
    print(dx5, dx10)
    numerical_differentiation()
