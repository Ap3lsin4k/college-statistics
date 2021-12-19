import math
from fractions import Fraction as F
from numbers import Rational, Real, Integral, Number
from typing import Union


def braces(decorated):
    def put_braces(original: 'PiRadians'):
        return "(" + decorated(original) + ")"

    return put_braces


class PiRadians(Number):
    def __hash__(self) -> int:
        return hash(self.number_of_semicircle_turns)

    def __init__(self, number_of_half_circle_turns: F, error=0):
        self.number_of_semicircle_turns = number_of_half_circle_turns.limit_denominator()
        self.error = self.number_of_semicircle_turns - number_of_half_circle_turns

    @classmethod
    def pi(cls):
        return cls(F(1))

    @classmethod
    def from_float_radians(cls, radians: float):
        num_of_turns = F.from_float(radians / math.pi)
        pi_radians = cls(F(num_of_turns))
        pi_radians.error = pi_radians.number_of_semicircle_turns - radians / math.pi  # abs(pi_radians.number_of_semicircle_turns - int(pi_radians.number_of_semicircle_turns))
        return pi_radians

    def __floordiv__(self, number_of_half_circle_turns):
        return PiRadians(number_of_half_circle_turns)

    def __truediv__(self, number_of_half_circle_turns: int):
        return PiRadians(self.number_of_semicircle_turns/number_of_half_circle_turns)

    def __eq__(self, other: 'PiRadians'):
        if isinstance(other, PiRadians):
            return self.number_of_semicircle_turns == other.number_of_semicircle_turns
        return self.number_of_semicircle_turns == other

    @property
    def numerator(self):
        return self.number_of_semicircle_turns.numerator

    @property
    def denominator(self):
        return self.number_of_semicircle_turns.denominator

    def __to_str(self, turns: F):
        numerator = "" if turns.numerator == 1 else f"{turns.numerator}"
        denominator = "" if turns.denominator == 1 else f"/{turns.denominator}"
        return numerator + "π" + denominator

    def __str__(self, turns=None):
        if turns:
            return self.__to_str(turns)
        return self.__to_str(self.number_of_semicircle_turns)

    @braces
    def __repr__(self) -> str:
        presentation = {str(self), f"{round(math.pi * self.number_of_semicircle_turns, 2)}"}
        if self.denominator > 100:
            approximation = self.number_of_semicircle_turns.limit_denominator(24)
            presentation.add(PiRadians.__str__(self, turns=approximation))
            presentation.add(f"{round(self.number_of_semicircle_turns * 180.)}°")
        error = f" ± {self.error}" if abs(self.error) > 10 ** 12 else ""
        return " = ".join(presentation) + error

    def __sub__(self, other: 'PiRadians'):
        return self.__add__(-other)

    def __neg__(self) -> 'PiRadians':
        return PiRadians(-self.number_of_semicircle_turns)

    def __add__(self, other: 'PiRadians'):
        return PiRadians(other.number_of_semicircle_turns+self.number_of_semicircle_turns)

    def __mul__(self, other: Union[Integral, Rational]):
        if isinstance(other, int):
            return PiRadians(self.number_of_semicircle_turns * other)
        raise TypeError(f"unsupported operand type(s) for *: \"{PiRadians.__name__}\" and \"{other.__class__.__name__}\"")

    def __rmul__(self, other: Union[Integral, Rational]):
        if isinstance(other, Union[Integral, Rational]):
            return self.__mul__(other)
        raise TypeError(f"unsupported operand type(s) for *: \"{other.__class__.__name__}\" and \"{PiRadians.__name__}\"")

    @classmethod
    def from_complex(cls, z: complex):
        try:
            return cls.from_float_radians(math.atan2(z.imag, z.real))
        except ZeroDivisionError:
            return cls(F(1, 2))


angle = PiRadians.from_complex
