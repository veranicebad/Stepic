from random import random
from random import seed
from math import sqrt
from random import gauss

def linear_regression_test(x, eff1, eff2):
    lst1 = []
    lst2 = []
    for i in range(100):
        scale = gauss(0,0.1) + 2
        y = x * scale + gauss(0, 0.005)
        z = x * scale + gauss(0, 0.005)
        for j in range(12):
            seed()
            k = (gauss(1, 0.05))
            y *= (eff1 * (k))
            k = (gauss(1, 0.005))
            z *= (eff2 * (k))
        lst1.append(y)
        lst2.append(z)
    print
    print
    print lst1
    print
    print
    print lst2

linear_regression_test(1.01, 1.5, 1.6)