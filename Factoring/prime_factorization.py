from time import time


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

            if is_prime(split[0]) and is_prime(split[1]):
                ends.append(split[1])
                break

        return ends


t1 = time()
print(prime_factors(-2))
t2 = time()

print(f"Factorization took {t2 - t1} secs")
