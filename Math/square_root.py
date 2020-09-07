from math import sqrt
from time import time


def square_root(n, decimal_places=15):
    lower = n / 4
    while 1:
        upper = n / lower
        lower = (lower + upper) / 2
        if round(lower, decimal_places) == round(upper, decimal_places):
            break
    return round(lower, decimal_places)


t1 = time()
print(square_root(1297461924192641926412417))
t2 = time()

print(f'Calculation took {t2 - t1} seconds.')
