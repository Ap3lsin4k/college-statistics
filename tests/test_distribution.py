import statistics
from collections.abc import Iterable
from fractions import Fraction
from math import sqrt

import pytest

from src.distribution import Distribution
from src.event import Event
from statistics import NormalDist


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
    assert pytest.approx(snake_special.std_dev, 0.01) == sqrt(
        (-0.88) ** 2 * 0.28 + (2 - 1.88) ** 2 * 0.28 + (5 / 2 - 1.88) ** 2 * .32)


def test_breakfast_cereal_producer():
    flakes = Distribution(370, 24)
    raisins = Distribution(170, 7)
    total = flakes + raisins
    assert total.mean == 540
    assert total.std_dev == 25
    assert total.z(575) == Fraction(7 / 5)


def test_integer_dataset():
    d = Distribution.from_small_sample(7, 2, 4, 3)

    assert 4 == d.mean
    assert Fraction(6, 4) == d.mean_absolute_deviation

    d = Distribution.from_small_sample(5, 3, 3, 5)
    assert 4 == d.mean


def test_distribution():
    d = Distribution.from_small_sample(8, 8, *[11] * 4, *[14] * 4)
    assert 11.6 == 58. / 5
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

    assert s.failure + s.success * s.failure == pytest.approx(s.probability_of_at_least_one_failure_in(2))
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
        assert n * p == 14
        return MuavraLaplasa(n, ) - MuavraLaplasa()

    # P(0.65, x, 0.75)


def test_normal():
    n = 10
    a = [m ** 2 / (n * m / n) for m in (3, 3, 4)]
    print(sum(a) - n)
    n = 11
    a = [6 * 6. / (n * p) for p in (3, 3, 5)]
    print(sum(a) - n)


def test_empirical_rule():
    lifespan = Distribution(16, 1.7)
    assert 16 == 14.3 + 1.7
    assert 16 == 19.4 - 1.7 - 1.7
    assert lifespan.probability(0, 14.3) == pytest.approx(0.50 - 0.68 / 2)
    assert lifespan.probability(0, 16) == pytest.approx(.5)
    assert lifespan.probability(0, 19.4) == pytest.approx(.5 + 0.95 / 2)
    assert lifespan.probability(14.3, 19.4) == 0.815


def test_empirical_rule2():
    lifespan = Distribution(87, 8)
    assert 87 + 24 == 111
    import scipy.stats as st
    # assert st.norm.cdf(0) == 0
    from statistics import NormalDist
    assert NormalDist().cdf(0) * 2 - 1 == 0  # *2 - 1

    # 1.9599639845400536
    # NormalDist().cdf
    #     assert 0 == st.norm.ppf(0.01)
    #
    #
    #     assert 0, st.norm.cdf(87/8)
    #     assert 0, st.norm.cdf(87/8)
    assert 16 == 19.4 - 1.7 - 1.7
    assert lifespan.probability(0, 14.3) == pytest.approx(0.50 - 0.68 / 2)
    # assert lifespan.probability(0, 16) == pytest.approx(.5)
    # assert lifespan.probability(0, 19.4) == pytest.approx(.5 + 0.95/2)
    # assert lifespan.probability(14.3, 19.4) == 0.815


class Sample(Iterable):
    def __iter__(self):
        for element in self.sample:
            yield element

    def __init__(self, *sample):
        self.sample = tuple(sorted(sample))
        if len(self.sample) <= 2:
            raise ValueError("too few params")

    def __repr__(self):
        if len(self.sample) <= 6:
            return str(self.sample)
        return f"|{self.sample}| == {len(self.sample)}"

    def __str__(self):
        return f"Sample(*{self.sample})"

    def __eq__(self, other):
        return self.sample == other

    def __len__(self):
        return len(self.sample)

    @property
    def n(self):
        return len(self)

    def split_3_intervals(self, bound1, bound2):
        if {bound1, bound2}.intersection(self.sample):
            raise ValueError("pick another boundary")
        # self.bound1, self.bound2 =

    @property
    def stddev(self):
        return statistics.stdev((self.sample))

    @property
    def mean(self):
        distribution = NormalDist.from_samples(self.sample)
        return distribution.mean

    def probability(self, boundary1, boundary2):
        from statistics import NormalDist
        distribution = NormalDist.from_samples(self.sample)
        return distribution.cdf(boundary2) - distribution.cdf(boundary1)

    def probability2(self, boundary1, boundary2):
        from statistics import NormalDist
        distribution = NormalDist.from_samples(self.sample)
        return F((boundary2 - self.mean) / self.stddev) - F((boundary1 - self.mean) / self.stddev)
        # return F(boundary2-distribution.mean) - distribution.cdf(boundary1-)


def F(x):
    """standart normal distribution"""
    from statistics import NormalDist
    return NormalDist().cdf(x) - 0.5
    # *2 - 1


class ChiSquaredTest:
    def __init__(self, s: Sample, boundaries: set):
        self.p1 = 1.0
        self.p2 = 0
        self.p3 = 0

        self.s = s

        if boundaries.intersection(self.s) or len(boundaries) != 2:
            raise ValueError("pick another boundary")

        self.boundary1 = min(boundaries)
        self.boundary2 = max(boundaries)

    @property
    def first(self):
        return [el for el in self.s if el < self.boundary1]

    @property
    def m1(self):
        return len(self.first)

    @property
    def second(self):
        return [el for el in self.s if self.boundary1 < el < self.boundary2]

    @property
    def m2(self):
        return len(self.second)

    @property
    def third(self):
        return [el for el in self.s if self.boundary2 < el]

    @property
    def m3(self):
        return len(self.third)

    @property
    def n(self):
        return len(self.s)


def test_sample():
    assert Sample(3, 2, 1) == (1, 2, 3)

    s = Sample(1, 2, 3)
    with pytest.raises(ValueError):
        ChiSquaredTest(s, {1, 3})
    s = Sample(3, 5, 8, 9, 10, 10, 11, 12, 14, 17)
    s = Sample(*(157, 159, 167, 170, 174, 174, 176, 178))
    # s.split_3_intervals()
    assert len(s) == 8


def test_chi_squared():
    chi = ChiSquaredTest(Sample(1, 3, 5), {2, 4})
    assert chi.boundary1 == 2
    assert chi.boundary2 == 4
    assert chi.m1 + chi.m2 + chi.m3 == 3
    chi = ChiSquaredTest(Sample(1, 3, 3, 5), {2, 4})
    assert chi.m2 == 2

    chi = ChiSquaredTest(Sample(1, 2, 3), {4, 5})
    assert chi.p1 == 1.00
    assert chi.p2 == 0
    assert chi.p3 == 0


def P(param, param1):
    pass


class Interval:
    def __init__(self, *sample):
        pass


def test_P():
    interval = Distribution.from_small_sample(9, 10, 12)
    # assert 0, statistics.pstdev((5, 6, 7, 9, 10, 11, 12, 16))
    s = Sample(5, 6, 7, 9, 10, 11, 12, 14, 16)
    assert 3.67 < s.stddev <= 3.73
    assert s.probability(8, 13) == pytest.approx(0.49 + .008, .01)

    assert F(0) == 0
    assert F(0.81) == pytest.approx(0.29, 0.01)
    assert F(1) == pytest.approx(0.68 / 2, .01)
    assert F(2) == pytest.approx(0.9544 / 2, .01)
    assert F(3) == pytest.approx(0.9972 / 2, .01)
    assert F(-1) == -F(1)
    assert F(-2) == -F(2)
    assert F(-3) == -F(3)
    infinity = 2 ** 128
    assert F(infinity) == 0.5
    assert F(-infinity) == -0.5
    assert s.mean == 10
    assert s.probability(8, 13) == pytest.approx(F((13 - 10) / 3.73) - F((8 - 10) / 3.73), 0.1)
    assert s.probability(8, 13) == s.probability2(8, 13)


class ChiSquaredTestOfHomogeneity:
    def __init__(self, girls: Sample, boys: Sample, boundaries: set):
        self.l = len(boundaries) + 1
        self.girls = ChiSquaredTest(girls, boundaries)
        self.boys = ChiSquaredTest(boys, boundaries)

    def __call__(self):
        return self.girls.n * self.boys.n * (self.first + self.second + self.third)

    @property
    def first(self):
        return self.jtol(self.girls.m1, self.boys.m1)

    def jtol(self, girls_m_j, boys_m_j):
        return (girls_m_j / self.girls.n
                - boys_m_j / self.boys.n) ** 2 \
               / (girls_m_j + boys_m_j)

    @property
    def second(self):
        return self.jtol(self.girls.m2, self.boys.m2)

    @property
    def third(self):
        return self.jtol(self.girls.m3, self.boys.m3)

def test_height_dist():
    girls = s = Sample(157, 159, 167, 170, 174, 174, 176, 178)
    boys = Sample(171, 173, 175, 176, 179, 180, 180, 180, 186, 190)
    assert 169.375 == girls.mean
    bs = {172, 175.5}
    g = ChiSquaredTest(girls, bs)
    b = ChiSquaredTest(boys, bs)
    assert g.m1 == 4
    assert b.m1 == 1
    chi = ChiSquaredTestOfHomogeneity(girls, boys, bs)
    assert pytest.approx(chi.first) == Fraction((Fraction(4 / 8) - Fraction(1 / 10)) ** 2, g.m1 + b.m1) * 1.
    assert chi() == 4.41

    assert g.m2 == 2
    assert b.m2 == 2

    assert g.m3 == 2
    assert b.m3 == 7
    # assert chi() % len(girls) == 0
    # assert chi() % len(boys) == 0
    assert chi.l == 3
    assert 3 / 2 == 1.5
    # Test NK Homogeneneous distribution
