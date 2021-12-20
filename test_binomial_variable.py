import math
from fractions import Fraction
from math import sqrt
from statistics import NormalDist

import numpy as np
import pytest

from src.bin import BinomialVariable
from src.sample import Sample
import matplotlib.pyplot as plt


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


# def test_noah():
#     assert 0, 4*2*7*8
#     assert 0, 0.95**10

def test_north():
    n = [
        [115, 200-115, 200],
        [21, 36-21, 36],
        [136, 100, 236],
        ]
    for i in range(3):
        assert n[i][0] + n[i][1] == n[i][2]
    assert n[1][0] + n[1][1] == n[1][2]
    assert n[2][0] + n[2][1] == n[2][2]

def test_binomial():
    assert Fraction(2,3)+ Fraction(1,3)*Fraction(1,5) == Fraction(11, 15)
    s = Sample(3, 5, 6, 7, 9, 6, 8)
    assert s.mean == pytest.approx(6.4, .1)

    assert BinomialVariable(500, 0.04)


def test_sm():
    import random
    distribution = dict()
    size = 10000
    for i in range(size):
        flips = list(random.choice([-1, 1]) for i in range(64))

        s = sum(flips)
        # print(flips)
        nd = NormalDist.from_samples(flips)
        # print(f"stddev: {nd.stdev}")
        distribution[s] = distribution.get(s, 0) + 1

    D = {key : int(distribution[key]/2) for key in sorted(distribution)} # {u'Label1': 26, u'Label2': 17, u'Label3': 30}
    plt.bar(*zip(*D.items()))
    # plt.xticks(np.arange(-20, 20, 2), np.arange(-20, 20, 2))
    # plt.show()
    # plt.savefig("sum_of_64_coin_flips_distribution.png")

