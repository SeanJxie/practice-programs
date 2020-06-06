from math import *
from numpy import arange

"""

Function object

"""


class Function:
    def __init__(self, expression, domain, precision):
        self.expression = expression
        self.domain = domain
        self.precision = precision

    def _output(self, x):
        x_val = self.expression.replace('x', str(x))

        try:
            return eval(x_val)

        except ValueError:  # Math domain error
            return None

    def get_point_set(self):

        point_set = []

        for x in arange(self.domain[0], self.domain[1] + self.precision, self.precision):
            point_set.append([x, self._output(x)])

        return point_set
