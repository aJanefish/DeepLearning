"""
神经网络Demo1
"""
import numpy as np


def init_network():
    net_work = {}
    # print(net_work)
    net_work['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    net_work['B1'] = np.array([0.1, 0.2, 0.3])
    net_work['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    net_work['B2'] = np.array([0.1, 0.2])
    net_work['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    net_work['B3'] = np.array([0.1, 0.2])
    # print(net_work)
    return net_work


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def identity_function(x):
    return x


def softmax(x):
    max = np.max(x)
    exp_a = np.exp(x - max)
    exp_sum = np.sum(exp_a)
    y = exp_a / exp_sum
    return y


def forward(net_work, x):
    W1, W2, W3 = net_work['W1'], net_work['W2'], net_work['W3']
    b1, b2, b3 = net_work['B1'], net_work['B2'], net_work['B3']
    # print("b1", b1)
    # print("b2", b2)
    # print("b3", b3)

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    # print(z1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    # print(z2)

    a3 = np.dot(z2, W3) + b3
    # y = identity_function(a3)
    y = softmax(a3)
    # print(y)
    return y


if __name__ == '__main__':
    netwotk = init_network()
    y = forward(netwotk, np.array([1.0, 0.5]))
    print("y =", y, np.sum(y))

    y = forward(netwotk, np.array([-1.0, - 0.5]))
    print("y =", y, np.sum(y))
    pass
