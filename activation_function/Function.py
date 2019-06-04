import numpy as np
import matplotlib.pyplot as plt


def step_function_one(x):
    """
    阶跃函数 版本实现1
    """
    y = x > 0
    print(y)
    return y.astype(np.int)


def step_function_two(x):
    """
    阶跃函数 版本实现2
    """
    return np.array(x > 0, np.int)


def test_step_function():
    arr = np.arange(-5.0, 5.0, 0.1)
    print(arr)
    arr1 = step_function_one(arr)
    print(arr1)
    plt.plot(arr, arr1)
    plt.ylim(-0.1, 1.1)  # 指定Y轴的范围
    plt.title('step_function')
    plt.show()


def sigmoid(x):  # sigmoid 函数
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def test_relu():
    arr = np.arange(-5.0, 5.0, 0.1)
    print(arr)
    arr1 = relu(arr)
    print(arr1)
    plt.plot(arr, arr1)
    # plt.ylim(-0.1, 1.1)  # 指定Y轴的范围
    plt.title('relu')
    plt.show()


def test_sigmoid():
    arr = np.arange(-5.0, 5.0, 0.1)
    print(arr)
    arr1 = sigmoid(arr)
    print(arr1)
    plt.plot(arr, arr1)
    plt.ylim(-0.1, 1.1)  # 指定Y轴的范围
    plt.title('sigmoid')
    plt.show()


def test_sigmoid_and_step_function():
    arr = np.arange(-5.0, 5.0, 0.1)
    print(arr)
    sd = sigmoid(arr)
    step = step_function_one(arr)
    print(sd)
    plt.plot(arr, sd, label="sigmoid")
    plt.plot(arr, step, linestyle="--", label="step function")
    plt.ylim(-0.1, 1.1)  # 指定Y轴的范围
    plt.title('sigmoid & step function')
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def test():
    flag = 3
    if flag == 1:
        test_step_function()
    elif flag == 2:
        test_sigmoid()
    elif flag == 3:
        test_relu()
    else:
        test_sigmoid_and_step_function()
    pass


if __name__ == '__main__':
    test()
