import numpy as np
from numpy.polynomial import Polynomial
import math
def solution_station6(input):
# [0 ,0],
# [0.1, 0.0998],
# [0.2, 0.1987],
# [0.7, 0.6442],
# [0.8, 0.7174],
# [1, 0.8415],
# [1.2, 0.932],
# [1.3, 0.9636],
# [1.4, 0.9854],
# [1.6, 0.9996],
# [2, 0,9093],
# [2.1, 0.8632],
# [2.5, 0.5985],
# [2.7, 0.4274],
# [2.9, 0.2392]
    return math.sin(input)

if __name__ == "__main__":
    print(solution_station6(0.7))
