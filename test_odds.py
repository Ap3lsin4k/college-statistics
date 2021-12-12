from fractions import Fraction

import pytest

Odds = Fraction


class BayesFactor:
    def __init__(self,  factor):
        self.factor = factor

    @classmethod
    def from_sensitivity_and_fpr(cls, sensitivity, false_positive_rate):
        return cls(sensitivity/false_positive_rate)

    def __mul__(self, other: Fraction):
        return self.factor * Fraction(other.numerator, other.denominator)

    @classmethod
    def from_specificity_and_fnr(cls, specificity, false_negative_rate):
        return cls(false_negative_rate/specificity)

    @property
    def error(self):
        return self.factor - int(self.factor)


def test_odds():

    factor = BayesFactor.from_sensitivity_and_fpr(sensitivity=0.9, false_positive_rate=0.09)
    assert factor.error == 0
    assert factor * Odds(1, 9) == pytest.approx(Odds(10, 9), 0.1)
    cancer_not_detected = BayesFactor.from_specificity_and_fnr(specificity=0.91, false_negative_rate=.10)
    assert 0 <= cancer_not_detected.error <= 0.11
    assert cancer_not_detected * Odds(1, 9) == pytest.approx(Odds(1, 9)*Odds(1, 9), 0.1)
