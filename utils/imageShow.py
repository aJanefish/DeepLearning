"""
显示图片
"""

import matplotlib.pyplot as plt
from matplotlib.image import imread

if __name__ == '__main__':
    img = imread('icons.png')
    plt.imshow(img)
    plt.show()
