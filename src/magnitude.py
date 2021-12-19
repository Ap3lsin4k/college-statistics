import math


class Magnitude:
    @classmethod
    def from_complex(cls, z: complex):
        return abs(z)

distance = Magnitude.from_complex
