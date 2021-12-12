import math
from fractions import Fraction as F


def braces(decorated):
    def put_braces(original: 'PiRadians'):
        return "(" + decorated(original) + ")"

    return put_braces


class PiRadians:
    def __init__(self, number_of_half_circle_turns: F, error=0):
        self.number_of_semicircle_turns = number_of_half_circle_turns
        self.error = error

    @classmethod
    def pi(cls):
        return cls(F(1))

    @classmethod
    def from_float_radians(cls, radians: float):
        num_of_turns = F.from_float(radians / math.pi).limit_denominator()
        pi_radians = cls(F(num_of_turns))
        pi_radians.error = pi_radians.number_of_semicircle_turns - radians / math.pi  # abs(pi_radians.number_of_semicircle_turns - int(pi_radians.number_of_semicircle_turns))
        return pi_radians

    def __floordiv__(self, number_of_half_circle_turns):
        return PiRadians(number_of_half_circle_turns)

    def __truediv__(self, number_of_half_circle_turns):
        return PiRadians(F(1, number_of_half_circle_turns))

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

    def __sub__(self, other):
        return self.number_of_semicircle_turns - other.number_of_semicircle_turns

    def __mul__(self, other):
        return self.number_of_semicircle_turns * other
