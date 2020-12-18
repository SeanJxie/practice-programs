import math

"""

Linearization/Euler's method for solving differential equations

"""


def euler(d, i_x, i_y, h, n) -> tuple:
    points = []
    x, y = i_x, i_y
    for _ in range(n):
        points.append((x, y, d(x, y)))
        y += h * d(x, y)
        x += h

    points.append((x, y, d(x, y)))
    return tuple(points)


def derivative(x, y):
    return x - y ** 2


print(euler(derivative, 1, 0, 0.2, 5))
