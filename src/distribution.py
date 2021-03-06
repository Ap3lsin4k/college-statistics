from fractions import Fraction
from math import sqrt
from typing import Iterable

from src.event import Event


class Distribution:
    def __init__(self, mean, standard_deviation):
        self.std_dev = standard_deviation
        self.mean = mean
        self.mean_absolute_deviation = None

    def __add__(self, other):
        return Distribution(self.mean + other.mean, sqrt(self.std_dev ** 2 + other.std_dev ** 2))

    def __sub__(self, other):
        return Distribution(self.mean - other.mean, sqrt(self.std_dev ** 2 + other.std_dev ** 2))

    def z(self, other_mean=0):
        return (other_mean - self.mean) / self.std_dev

    def __str__(self):
        return f"m={self.mean}, std_dev:{self.std_dev}"

    @classmethod
    def from_table(cls, *args):
        one_hundred_percents = sum(event.probability for event in args)
        if one_hundred_percents != 1:
            raise ValueError("overall probability must be 100%")

        # weighted average
        mean = sum(event.event_value * event.probability for event in args)

        variance = Distribution.variance(mean, events=args)
        return Distribution(
            mean=mean,
            standard_deviation=sqrt(variance))

    @staticmethod
    def variance(mean, events: Iterable[Event]):
        return sum((mean - event.event_value) ** 2 * event.probability for event in events)

    @classmethod
    def from_small_sample(cls, *args) -> 'Distribution':
        # actually there is a constant for calculating std deviation
        for argument in args:
            assert isinstance(argument, int)

        d = Distribution(Fraction(sum(args), len(args)), None)
        d.mean_absolute_deviation = Fraction(sum(abs(value - d.mean) for value in args), len(args))
        return d

    def probability(self, a, b):
        if a == 0:

            num_of_std_dev = round((b - self.mean) / self.std_dev)
            empirical_rule = {0: 0, 1: 0.68, 2: 0.95}

            if num_of_std_dev < 0:
                return 0.5 - empirical_rule[1] / 2

            return 0.5 + empirical_rule[num_of_std_dev] / 2

        return self.probability(0, b) - self.probability(0, a)


    def num_of_std_dev(self, a, b):
        return None
