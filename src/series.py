from fractions import Fraction

import numpy as np
import pytest
# from sage.structure.sage_object import SageObject

class Series:
    infinity = 1000

    def __init__(self, a=lambda n: Fraction(), infinity_power=0, rang=None):
        self.a = a

        if infinity_power:
            self.infinity = 10 ** infinity_power

        if not rang:
            rang = range(1, self.infinity)

        self._value = sum(self.a(n) for n in rang)

        self.diverges = self._value == float('inf')

    def doit(self, infinity):
        return sum(self.a(n) for n in range(1, infinity))

    def __eq__(self, other):
        return pytest.approx(self._value, 0.1) == other

    def __repr__(self):
        return str(float(self._value))

    def __str__(self):
        return repr(self)+" = "+" + ".join(map(str, [self.a(n) for n in range(0, 12)])) + " + ..."

    def __iter__(self):
        self.elem_index = 0
        return self

    def __next__(self):
        self.elem_index += 1
        return self.a(self.elem_index)


class PartialSum:
    def __init__(self, finite_sum):
        def a(n):
            if n < 1:
                raise ValueError("Indexing starts from 1")
            if n == 1:
                return finite_sum(1)
            else:
                return finite_sum(n) - finite_sum(n - 1)

        self.a = a

        self.series = None  # Series(finite_sum)
    #
    # def a(self, param):
    #     pass
