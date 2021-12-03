import math
from fractions import Fraction
from math import sqrt

import pytest

from src.bin import BinomialVariable


def test_binomial_variable():
    with pytest.raises(ValueError):
        BinomialVariable(1, 1.1)
    with pytest.raises(ValueError):
        BinomialVariable(0, 1.1)

    bin = BinomialVariable(1, .5)
    assert bin.mean == .5
    assert bin.variance == .5*.5
    assert bin.stddev == .5


def test_binomial_variable2():
    bin = BinomialVariable(2, .6)
    assert bin.mean == 1.2
    assert bin.variance == 2 * .6 * .4
    assert bin.stddev == sqrt(.48) == pytest.approx(0.69282)

    bin = BinomialVariable(15, .3)
    assert bin.mean == 4.5
    assert bin.stddev == pytest.approx(1.77, 0.01)

    questions = 20
    bin = BinomialVariable(number_of_trials=questions, probability_of_success=Fraction(1, 5))
    assert bin.mean == 4
    assert bin.variance == pytest.approx(20*Fraction(1, 5)*.8) == 3.2
    assert bin.stddev == sqrt(3.2) == pytest.approx(1.79, 0.01)


def test_a():
    lambd = 1 / 2. # 1 person per two minutes
    t = 9 # minutes
    def P(k):
        events = k
        return ((lambd * t) **k / math.factorial(k)) * math.e**(-lambd*t)
    for k in range(10):
        print(k, round(P(k), 3))

    print(1-P(0) - P(1)- P(2) - P(3) - P(4))

# 0 0.011
# 1 0.05
# 2 0.112
# 3 0.169
# 4 0.19
# 5 0.171
# 6 0.128
# 7 0.082
# 8 0.046
# 9 0.023
# 0.4678964236252844
