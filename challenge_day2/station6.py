import numpy as np
from numpy.polynomial import Polynomial

def solution_station6(input):

    x = np.array([0.6, 0.3, 2.8, 1.7, 1.4, 2.5, 2.2, 0, 2.6, 2.4, 2.9])
    y = np.array([0.5646, 0.2955, 0.335, 0.9917, 0.9854, 0.5985, 0.8085, 0, 0.5155, 0.6755, 0.2392])
    p = Polynomial.fit(x, y, deg=4)
    print(p.convert())   # readable coefficients, lowest power first
    print(p(input))

if __name__ == "__main__":
    solution_station6(58)
