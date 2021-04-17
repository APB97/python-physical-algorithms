from math import sqrt


def bukin_n6(xx):
    x1 = xx[0]
    x2 = xx[1]

    term1 = 100 * sqrt(abs(x2 - 0.01 * x1 ** 2))
    term2 = 0.01 * abs(x1 + 10)
    value = term1 + term2
    return value


if __name__ == "__main__":
    print(bukin_n6([-12, -2]))
