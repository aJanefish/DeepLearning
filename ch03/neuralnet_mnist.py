"""
手写数字识别
"""
import pickle

import numpy as np
from PIL import Image

from dataset.mnist import load_mnist


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    print("network", type(network))
    return network


def show_tips(name, x):
    print(name, " = ", type(x), x.ndim, x.shape)


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    show_tips("x_test", x_test)
    show_tips("t_test", t_test)
    return x_test, t_test


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    max = np.max(x)
    exp_a = np.exp(x - max)
    exp_sum = np.sum(exp_a)
    y = exp_a / exp_sum
    return y


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    # show_tips("W1", W1)
    # show_tips("W2", W2)
    # show_tips("W3", W3)
    # show_tips("b1", b1)
    # show_tips("b2", b2)
    # show_tips("b3", b3)

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    # print("z1", z1.shape)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    # print("z2", z2.shape)

    a3 = np.dot(z2, W3) + b3

    y = softmax(a3)
    # print("y", y.shape)
    return y


def img_show(img):
    img = img * 255
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def show(img):
    img = img.reshape(28, 28)  # 把图像的形状变为原来的尺寸
    img_show(img)


if __name__ == '__main__':
    network = init_network()
    x_test, t_test = get_data()

    accuracy_cnt = 0
    for i in range(len(x_test)):
        y = predict(network, x_test[i])
        p = np.argmax(y)
        if p == t_test[i]:
            accuracy_cnt += 1

    print("Accuracy:" + str(float(accuracy_cnt) / len(x_test)))

    pass
