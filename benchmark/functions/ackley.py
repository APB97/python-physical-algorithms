from math import pi, cos, exp, sqrt


def ackley(xx, a=20, b=0.2, c=2*pi):
    d = len(xx)

    sum1 = sum([x ** 2 for x in xx])
    sum2 = sum([cos(c * x) for x in xx])

    term1 = -a * exp(-b * sqrt(sum1 / d))
    term2 = -exp(sum2/d)

    y = term1 + term2 + a + exp(1)
    return y
