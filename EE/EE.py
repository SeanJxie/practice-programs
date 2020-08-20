from itertools import combinations

"""

Tools for Extended Essay tests.

"""


def appearances_in_combo_subset(original_set, subset_size, element):
    combos = list(combinations(original_set, subset_size))

    count = 0
    for combo in combos:
        if element in combo:
            print(combo)
            count += 1

    return count


def sets_which_obtain_r(original_set, subset_size, r):
    combos = list(combinations(original_set, subset_size))
    sets = []
    count = 0

    for combo in combos:
        res = 1

        for element in combo:
            res *= element

        if res == r:
            sets.append(combo)
            count += 1

    print(count)
    return sets



def set_combo_intersect(s1, s2):
    intersections = 0

    for combo1 in s1:
        for combo2 in s2:
            if combo1 == combo2:
                intersections += 1
                print(combo1)

    return intersections


def factors(n):
    f = []

    temp = 1

    while temp <= n:
        if n % temp == 0:
            f.append(temp)

        temp += 1

    return f


def generate_deck():
    deck = []

    for i in range(1, 14):
        deck += [i, i, i, i]

    return deck


s = []
for c in sets_which_obtain_r(generate_deck(), 4, 24):
    if c not in s:
        s.append(c)


print(s)
