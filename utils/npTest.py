import numpy as np

"""
用NumPy生成数组
"""


def create():
    print("create array------ start")
    x = np.array([1, 2, 3])
    y = np.array([2, 4, 6])
    print("x =", x)
    print("y =", y)
    print(type(x))
    print("x + y =", x + y)
    print("x - y =", x - y)
    print("x * y =", x * y)
    print("x / y =", x / y)
    print("x / 2.0 =", x / 2.0)
    print("create array ------ end")


def arrayNN():
    print("N维数组测试----------start")
    AA = np.array([[1, 2], [3, 4]])
    print(AA)
    print(AA.shape, AA.size, AA.dtype)
    BB = np.array([[3, 0], [0, 6]])
    print("AA + BB =", AA + BB)
    print("AA * BB =", AA * BB)
    print("AA * 10 =", AA * 10)

    X = np.array([[51, 55], [14, 19], [0, 4]])
    print(X)
    print(X[0], X[0][1])
    for row in X:
        print(row)

    X = X.flatten()  # 转化为一维数组
    print(X)
    # X = X > 15
    # print(X)
    # 数组中大于15
    X = X[X > 15]
    print(X)
    print("N维数组测试----------end")
    pass

    if __name__ == '__main__':
        print("Hello World!")
    create()
    arrayNN()
    pass
