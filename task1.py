import numpy as np
import math
from matplotlib import pyplot

from signals import linear_with_noise, linear


def is_pot(x: int):
    return x == 0 or (x & (x - 1)) == 0


def prepare_matrices(n):
    assert is_pot(n)

    level = int(math.log(n, 2)) + 1

    h = [1]
    NC = 1 / math.sqrt(2)
    LP = [1, 1]
    HP = [1, -1]

    for i in range(1, level):
        h = np.dot(NC, np.concatenate([np.matrix(np.kron(h, LP)), np.matrix(np.kron(np.eye(len(h)), HP))]))
    h = np.array(h)

    return h


def haar_1d(x):
    n = len(x)

    H = prepare_matrices(n)

    x = x[0:len(H)]

    y = H.dot(x)
    y = np.array(y)

    return y


def haar_1d_inverse(y):
    n = len(y)

    H = prepare_matrices(n)

    y = y[0:len(H)]

    x1 = H.transpose().dot(y.transpose())
    x1 = np.array(x1)

    return x1.transpose()


if __name__ == '__main__':
    signal = linear_with_noise()
    transformed = haar_1d(signal)
    reconstructed = haar_1d_inverse(transformed)

    assert all(signal.round(6) == reconstructed.round(6))

    # other = haar_1d_inverse(reconstructed)

    fig, axes = pyplot.subplots(1, 3, squeeze=False, figsize=(15, 12))

    axes[0, 0].plot(signal)
    axes[0, 1].plot(transformed)
    axes[0, 2].plot(reconstructed)
    # axes[0, 1].plot(other)
    pyplot.show()
