from time import time
import matplotlib.pyplot as plt
import numpy as np


def prime_factors(n):
    ends = []

    def pc_split(i):
        p = 2
        while i % p != 0:
            p += 1

        return p, i // p

    def is_prime(j):
        prime = True
        div = 2

        while div <= j ** (1 / 2):
            if j % div == 0:
                prime = False

            div += 1

        return prime

    if n <= 1:
        return None

    else:
        while 1:
            split = pc_split(n)
            n = split[1]
            ends.append(split[0])

            if is_prime(split[0]) and is_prime(n):
                ends.append(n)
                break

        return ends


def get_lowest(itr):
    i = 0

    while itr[i] != 0:
        i += 1

    return itr[i]


MAX = 12
c = 1

times = []
while c <= MAX:
    t1 = time()
    prime_factors(int('9' * c))
    t2 = time()

    times.append(t2 - t1)

    c += 1

x = np.array([n for n in range(1, MAX + 1)])
y = np.array(times)

plt.scatter(x, y)
plt.xlabel("# of 9's")
plt.ylabel("time (sec)")

print(get_lowest(times))

plt.show()
