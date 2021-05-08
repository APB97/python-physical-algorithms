from math import cos, pi


def rastrigin(xx):
    dimensions = len(xx)
    s = sum([x ** 2 - 10 * cos(2 * pi * x) for x in xx])

    y = 10 * dimensions + s
    return y
