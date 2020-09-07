import math

"""

Bunch of things to do with a number

"""


class Number:
    def __init__(self, value):
        """
        Represents a number.
        :param value: The value of the number.
        """
        self.value = value
        self.valid_types = (int, float)
        if type(value) not in self.valid_types:
            raise ValueError(f'Value not valid. Valid values are {self.valid_types}.')

    def get_type(self):
        """
        Get the type of self.value
        :return: Type of self.value.
        """
        return type(self.value)

    def prime_factors(self):
        """
        Obtain the prime factorization of self.value using a factor tree.
        :return: Prime factors of self.value as a tuple.
        """
        if self.get_type() == int:
            if self.value <= 1:
                return None
            else:
                ends = []
                while 1:
                    split = self._pc_split(self.value)
                    self.value = split[1]
                    ends.append(split[0])
                    if self._is_prime(split[0]) and self._is_prime(self.value):
                        ends.append(self.value)
                        break
                return tuple(ends)
        else:
            raise ValueError(f'Value of type {self.get_type()} cannot be factorized.')

    def factors(self):
        """
        Obtain all the factors of self.value from the exclusive range (1, self.value) via brute force.
        :return: All factors of self.value as a tuple.
        """
        if self.get_type() == int:
            factors = []
            i = 2
            while i <= self.value ** (1 / 2):
                if self.value % i == 0:
                    factors.append(i)
                i += 1
            return tuple(factors)
        else:
            raise ValueError(f'Value of type {self.get_type()} cannot be factorized.')

    def fraction_form(self):
        """
        Obtain self.value in a form a / b via the Farey algorithm to the accuracy of Python's float type.
        :return: Numerator and denominator (a, b) as a tuple, respectively.
        """
        if self.get_type() == float:
            # 0 / 1
            n1 = 0
            d1 = 1

            # 1 / 1
            n2 = 1
            d2 = 1
            f_part = self._fractional_part(self.value)
            while 1:
                mediant_frac = self._mediant(n1, d1, n2, d2)
                mediant_float = self._mediant(n1, d1, n2, d2)[0] / self._mediant(n1, d1, n2, d2)[1]
                if mediant_float < f_part:
                    n1, d1 = mediant_frac
                elif mediant_float > f_part:
                    n2, d2 = mediant_frac
                else:
                    return int(self.value - f_part) * d1 + n1, d1

        else:
            raise ValueError('Must be float to convert to fraction form.')

    @staticmethod
    def _pc_split(n):
        """
        The branching of a factor tree; split an integer n
        into a (prime, composite) or (prime, prime) pair.
        :param n: Integer to be split.
        :return: (prime, composite) or (prime, prime) pair as a tuple.
        """
        p = 2
        while n % p != 0:
            p += 1
        return p, n // p

    @staticmethod
    def _is_prime(n):
        """
        Check if an integer n is prime via semi brute-force.
        :param n: Integer to check.
        :return: If n is prime or not, as bool.
        """
        prime = True
        div = 2
        while div <= n ** (1 / 2):
            if n % div == 0:
                prime = False
            div += 1
        return prime

    @staticmethod
    def _fractional_part(n):
        """
        Obtain the fractional part of a float n given by f(x) = x - floor(x).
        :param n: Input
        :return: The fractional part of n as float
        """
        return n - math.floor(n)

    @staticmethod
    def _mediant(a1, b1, a2, b2):
        """
        By the mediant inequality: a1 / b1 < (a1 + a2) / (b1 + b2) < a2 / b2
        :param a1: Numerator 1
        :param b1: Denominator 1
        :param a2: Numerator 2
        :param b2: Denominator 2
        :return: The mediant of a1 / b1 and a2 / b2
        """
        return a1 + a2, b1 + b2


myNum = Number(value=math.pi)
print(myNum.fraction_form())
