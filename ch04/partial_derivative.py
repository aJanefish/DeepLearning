"""
偏导数
"""
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def function(x):
    return x[0] ** 2 + x[1] ** 2


def partial_derivative():
    # 绘制三维曲面
    fig = plt.figure()
    axes3d = Axes3D(fig)
    # !！面
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    print(x.ndim, x.shape)
    # print(x)

    X, Y = np.meshgrid(x, y)
    Z = X ** 2 + Y ** 2

    print(X.ndim, X.shape)
    print(Y.ndim, Y.shape)
    print(Z.ndim, Z.shape)
    axes3d.plot_surface(X, Y, Z)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    partial_derivative()
