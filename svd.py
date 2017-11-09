from scipy import misc
from PIL import Image
import numpy


def split(x, w, h):
    R = numpy.zeros(shape=(w, h))
    G = numpy.zeros(shape=(w, h))
    B = numpy.zeros(shape=(w, h))
    for i in range(0, w):
        for j in range(0, h):
            R[i][j] = x[i][j][0]
            G[i][j] = x[i][j][1]
            B[i][j] = x[i][j][2]

    return R, G, B


if __name__ == "__main__":
    im = Image.open('pic.png')
    width, height = im.size

    arr = misc.imread('pic.png')  # 640x480x3 array
    R, G, B = split(arr, width, height)
    
