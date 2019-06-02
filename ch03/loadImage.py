# coding: utf-8
import sys, os

sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
from dataset.mnist import load_mnist

from PIL import Image


# from PIL import Image


def img_show(img):
    img = img * 255
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def show(imgs):
    for x in range(10):
        img = imgs[x]
        img = img.reshape(28, 28)  # 把图像的形状变为原来的尺寸
        img_show(img)


def show_tips(name, x):
    print(name, " = ", type(x), x.ndim, x.shape)


(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)

show_tips("x_train", x_train)  # (60000,784) 总共有60000张图像,每张图像大小为28*28
show_tips("t_train", t_train)
show_tips("x_test", x_test)
show_tips("t_test", t_test)

img = x_train[0]
label = t_train[0]
print("label =", label)  # 5

print(img.shape)  # (784,)
# 把数组转化为举证
img = img.reshape(28, 28)  # 把图像的形状变为原来的尺寸
print(img.shape)  # (28, 28)

img_show(img)
# show(x_train)
