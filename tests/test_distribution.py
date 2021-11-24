from fractions import Fraction
from math import sqrt

import pytest

from src.distribution import Distribution
from src.event import Event


def test_init():
    adam = Distribution(175, 30)
    mike = Distribution(150, 40)
    d = adam - mike
    assert d.mean == 25
    assert d.std_dev == 50
    assert d.z() == -0.5


def test_quiz():
    bowling_buds = Distribution(610, 60)
    alleycasts = Distribution(630, 80)
    diff = alleycasts - bowling_buds
    assert diff.std_dev == 100


def test_quiz2():
    small = Event(2.0, .28)
    medium = Event(3, .4)
    large = Event(3.5, .32)

    with pytest.raises(ValueError):
        Distribution.from_table(small, medium)

    snake = Distribution.from_table(small, medium, large)
    assert 2.88 == pytest.approx(snake.mean)
    assert 0.59 == pytest.approx(snake.std_dev, .01)

    small_special = small
    small_special.event_value -= 1
    medium_special = medium
    medium_special.event_value -= 1
    large_special = large
    large_special.event_value -= 1

    snake_special = Distribution.from_table(small_special, medium_special, large_special)
    assert pytest.approx(snake_special.mean) == 1.88
    assert pytest.approx(snake_special.std_dev, 0.01) == sqrt((-0.88)**2*0.28 + (2-1.88)**2*0.28 + (5/2-1.88)**2*.32)


def test_breakfast_cereal_producer():
    flakes = Distribution(370, 24)
    raisins = Distribution(170, 7)
    total = flakes + raisins
    assert total.mean == 540
    assert total.std_dev == 25
    assert total.z(575) == Fraction(7/5)


def test_integer_dataset():
    d = Distribution.from_small_sample(7, 2, 4, 3)

    assert 4 == d.mean
    assert Fraction(6, 4) == d.mean_absolute_deviation

    d = Distribution.from_small_sample(5, 3, 3, 5)
    assert 4 == d.mean


def test_distribution():
    d = Distribution.from_small_sample(8, 8, *[11]*4, *[14]*4)
    assert 11.6 == 58./5
    assert 11.6 == float(d.mean)


class Success:
    def __init__(self, success):
        if 0 <= success <= 1:
            self.success = success
            self.failure = 1 - success
        else:
            raise ValueError

    def probability_no_failure_for(self, strike):
        return 1 - self.probability_of_at_least_one_failure_in(tries=strike)

    def probability_of_at_least_one_failure_in(self, tries):
        return self.failure * (1 - self.success ** tries) / self.failure



def test_range():
    with pytest.raises(ValueError):
        Success(1.01)
        Success(-.01)


def test_prob():
    s = Success(0.95)
    assert 1 - s.failure == s.probability_no_failure_for(1)
    assert s.failure == s.probability_of_at_least_one_failure_in(1)

    assert s.failure + s.success*s.failure == pytest.approx(s.probability_of_at_least_one_failure_in(2))
    # assert 1 - s.failure + s.success * s.failure + s.success ** 2 * s.failure == pytest.approx(s.probability_no_failure_for(3))





def test_exit_poll():
    def MuavraLaplasa():
        pass
    n = 20
    za = 14
    epsilon = 0.05
    def P(param, x, param1):
        p = 0.7
        n = za / p
        assert n*p == 14
        return MuavraLaplasa(n, ) - MuavraLaplasa()

    # P(0.65, x, 0.75)

def test_normal():
    n = 10
    a = [m**2/(n*m/n)  for m in (3, 3, 4)]
    print(sum(a) - n)
    n=11
    a = [6*6./(n*p)  for p in (3, 3, 5)]
    print(sum(a) - n)


def test_empirical_rule():
    lifespan = Distribution(16, 1.7)
    assert 16 == 14.3 + 1.7
    assert 16 == 19.4 - 1.7 - 1.7
    assert lifespan.probability(0, 14.3) == pytest.approx(0.50 - 0.68/2)
    assert lifespan.probability(0, 16) == pytest.approx(.5)
    assert lifespan.probability(0, 19.4) == pytest.approx(.5 + 0.95/2)
    assert lifespan.probability(14.3, 19.4) == 0.815


def test_empirical_rule2():
    lifespan = Distribution(87, 8)
    assert 87 + 24 == 111
    import scipy.stats as st
    # assert st.ppf
    assert 16 == 19.4 - 1.7 - 1.7
    assert lifespan.probability(0, 14.3) == pytest.approx(0.50 - 0.68/2)
    assert lifespan.probability(0, 16) == pytest.approx(.5)
    assert lifespan.probability(0, 19.4) == pytest.approx(.5 + 0.95/2)
    assert lifespan.probability(14.3, 19.4) == 0.815

