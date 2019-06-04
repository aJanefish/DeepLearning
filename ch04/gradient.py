"""
梯度
"""
import numpy as np


def gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]

        x[idx] = tmp_val + h
        fxh1 = f(x)
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)

        x[idx] = tmp_val
    return grad
    # pass


def functoin_2(x):
    # print(x)
    return np.sum(x ** 2)


def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = gradient(f, x)
        x -= lr * grad
        # print(x)
    return x


if __name__ == '__main__':
    grad = gradient(functoin_2, np.array([1.0, 2.0]))
    print(grad)
    grad = gradient(functoin_2, np.array([3.0, 5.0]))
    print(grad)

    grad = gradient(functoin_2, np.array([0.0, 0.5]))
    print(grad)
    print(grad.ndim, grad.shape)
    # ss = np.array([[1, 2, 3], [4, 5, 6]])
    # print(ss.size)
    inix_x = np.array([3.0, 4.0])
    reslut = gradient_descent(functoin_2, inix_x, lr=0.1, step_num=100)
    print("1",reslut)

    reslut = gradient_descent(functoin_2, inix_x, lr=10.0, step_num=100)
    print("2",reslut)

    reslut = gradient_descent(functoin_2, inix_x, lr=1e-10, step_num=100)
    print("3",reslut)
