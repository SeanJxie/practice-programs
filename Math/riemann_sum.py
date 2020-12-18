import math
from time import time

"""
Riemann sum algorithm
"""


def timed_function(f):
    def wrap(*arg):
        st = time()
        out = f(*arg)
        return out, time() - st

    return wrap


@timed_function
def riemann_sum(f, a, b, n):
    if n <= 0:
        raise ValueError("n cannot less than or equal to 0")
    delta_x = (b - a) / n
    area = 0
    for i in range(1, n + 1):  # Upper sum. Lower is given by range(n).
        area += f(a + i * delta_x) * delta_x
    return area


print(riemann_sum(lambda x: x, 0, 1, 1000))
