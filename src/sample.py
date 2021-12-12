import statistics
from fractions import Fraction
from statistics import NormalDist
from typing import Iterable

import pytest

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


def P(param, param1):
    pass


class Interval:
    def __init__(self, *sample):
        pass


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
        return (Fraction(girls_m_j, self.girls.n)
                - Fraction(boys_m_j, self.boys.n)) ** 2 \
               / (girls_m_j + boys_m_j)

    @property
    def second(self):
        return self.jtol(self.girls.m2, self.boys.m2)

    @property
    def third(self):
        return self.jtol(self.girls.m3, self.boys.m3)