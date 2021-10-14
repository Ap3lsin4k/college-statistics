from math import sqrt

import pytest


class Distribution:
    def __init__(self, mean, standard_deviation):
        self.std_dev = standard_deviation
        self.mean = mean

    def __sub__(self, other):
        return Distribution(self.mean-other.mean, sqrt(self.std_dev**2 + other.std_dev**2))

    def z(self):
        return -self.mean / self.std_dev

    @classmethod
    def from_table(cls, *args):
        one_hundred_percents = sum(event.probability for event in args)
        if one_hundred_percents != 1:
            raise ValueError("overall probability must be 100%")

        mean = sum(event.event_value*event.probability for event in args)
        variance = sum((mean - event.event_value)**2*event.probability for event in args)
        return Distribution(
            mean=mean,
            standard_deviation=sqrt(variance))


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
    small =Event(2.0, .28)
    medium = Event(3, .4)
    large = Event(3.5, .32)

    with pytest.raises(ValueError):
        Distribution.from_table(small, medium)

    snake = Distribution.from_table(small, medium, large)
    assert 2.88 == pytest.approx(snake.mean)
    assert 0.59 == pytest.approx(snake.std_dev, .03)


class Event():
    def __init__(self, value, probability):
        self.event_value = value
        self.probability = probability
