"""

Application of the Taylor series for approximating trigonometric functions

"""


def maclaurin_sin(v, n_terms):
    """
    Since sin(x) is infinitely differentiable at x=0,
    we are using the Maclaurin series instead.
    """

    def fact(i):
        p = 1
        for j in range(2, i + 1):
            p *= j
        return p

    # f^n(0) for f(x) = sin(x) cycles through the following sequence:
    derivative_seq = (
        0,  # sin(0)
        1,  # cos(0)
        0,  # -sin(0)
        -1,  # -cos(0)
    )
    approx = 0
    for n in range(n_terms + 1):
        approx += derivative_seq[n % 4] * v ** n / fact(n)

    return approx


def maclaurin_cos(v, n_terms):
    """
    Since cos(x) is infinitely differentiable at x=0,
    we are using the Maclaurin series instead.
    """

    def fact(i):
        p = 1
        for j in range(2, i + 1):
            p *= j
        return p

    # f^n(0) for f(x) = cos(x) cycles through the following sequence:
    derivative_seq = (
        1,  # cos(0)
        0,  # -sin(0)
        -1,  # -cos(0)
        0,  # sin(0)
    )
    approx = 0
    for n in range(n_terms + 1):
        approx += derivative_seq[n % 4] * v ** n / fact(n)

    return approx


print(maclaurin_cos(5, 100))
