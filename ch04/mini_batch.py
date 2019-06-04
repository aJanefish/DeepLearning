"""
mini_batch 学习
"""
import numpy as np

from dataset.mnist import load_mnist


def mini_batch():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
    print(x_train.shape)
    print(t_train.shape)

    train_size = x_train.shape[0]
    batch_size = 100
    batch_mark = np.random.choice(train_size, batch_size)
    # print(batch_mark.shape, batch_mark)
    x_batch = x_train[batch_mark]
    t_batch = t_train[batch_mark]
    print(x_batch.shape)
    print(t_batch.shape)
    pass


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]

    return -np.sum(t * np.log(y + 1e-7)) / batch_size


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


if __name__ == '__main__':
    mini_batch()

    print(np.float(1e-4))
