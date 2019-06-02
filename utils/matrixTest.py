import numpy as np


def dot(x, y):
    C = np.dot(x, y)
    print("X*Y=", C)
    D = np.dot(y, x)
    print("Y*X=", D)


def test1():
    A = np.array([[1, 2], [3, 4]])
    print(A.shape, A.size)
    B = np.array([[5, 6], [7, 8]])
    print(B.shape, B.size)
    dot(A, B)
    pass


def test2():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    print(A.shape, A.size)
    B = np.array([[1, 2], [3, 4], [5, 6]])
    dot(A, B)
    pass


if __name__ == '__main__':
    test1()
    test2()
    pass
