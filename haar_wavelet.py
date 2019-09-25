import matplotlib.pyplot as plt
import WorkWFiles
from tkinter import messagebox as mb

ORDER = 1


def haarFWT(signal, level):
    s = .5                 # scaling -- try 1 or ( 2 ** .5 )
    h = [1,  1]          # lowpass filter
    g = [1, -1]          # highpass filter
    f = len(h)           # length of the filter
    t = signal              # 'workspace' array
    l = len(t)              # length of the current signal
    y = [0] * l             # initialise output
    t = t + [0, 0]        # padding for the workspace

    for i in range(level):
        y[0:l] = [0] * l    # initialise the next level
        l2 = l // 2         # half approximation, half detail
        for j in range(l2):
            for k in range(f):
                y[j] += t[2*j + k] * h[k] * s
                y[j+l2] += t[2*j + k] * g[k] * s
        l = l2             # continue with the approximation
        t[0:l] = y[0:l]
    return y


def main():
    s0 = WorkWFiles.write_to_list('solution.dat')[4000:5000]
    plt.plot(s0)
    plt.plot((haarFWT(s0, ORDER)))
    plt.title('haar order=' + str(ORDER))
    plt.show()


if __name__ == "__main__":
    main()
