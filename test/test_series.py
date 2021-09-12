import pytest
from fractions import Fraction


class Series:
    infinity = 100

    def __init__(self, a):
        self.a = a
        self.value = sum([self.a(n) for n in range(1, 100)])

        self.diverges = self.value == float('inf')


    def __eq__(self, other):

        return pytest.approx(self.value, 0.1) == other


    def __repr__(self):
        return str(float(self.value))

    def __str__(self):
        return " + ".join(map(str, [self.a(n) for n in range(1, 10)])) + " + ..."

def test_series():
    s = Series(lambda n: Fraction(1, 2**n))
    assert s == s

    assert s == 1

    assert not s.diverges


