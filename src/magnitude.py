import math


class Magnitude:
    @classmethod
    def from_complex(cls, z: complex):
        return math.sqrt(z.real**2 + z.imag**2)

distance = Magnitude.from_complex
