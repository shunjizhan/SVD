from scipy import misc
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def split(x, w, h):
    R = np.zeros(shape=(w, h))
    G = np.zeros(shape=(w, h))
    B = np.zeros(shape=(w, h))
    for i in range(0, w):
        for j in range(0, h):
            R[i][j] = x[i][j][0]
            G[i][j] = x[i][j][1]
            B[i][j] = x[i][j][2]

    return R, G, B


def combine(R, G, B, w, h):
    result = np.zeros(shape=(w, h, 3))
    for i in range(0, w):
        for j in range(0, h):
            result[i][j][0] = R[i][j]
            result[i][j][1] = G[i][j]
            result[i][j][2] = B[i][j]

    return result


def best_k(A, k):
    U, s, V = np.linalg.svd(A, full_matrices=True)
    U_new = U[:, :k]
    S_new = np.diag(s[:k])
    V_new = V[:k, :]

    return (U_new.dot(S_new)).dot(V_new)


if __name__ == "__main__":
    pic = 'pic2.png'
    im = Image.open(pic)
    h, w = im.size

    arr = misc.imread(pic)  # 640x480x3 array
    R, G, B = split(arr, w, h)
    k = 10
    R_best, G_best, B_best = best_k(R, k), best_k(G, k), best_k(B, k)

    rbg_new = combine(R_best, G_best, B_best, w, h)
    # print rbg_new.shape
    plt.imshow(np.uint8(rbg_new))
    plt.show()
