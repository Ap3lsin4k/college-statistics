import math
from fractions import Fraction as F
from math import atan
from numbers import Real, Integral

import pytest

from src.magnitude import Magnitude
from src.rotation import PiRadians, angle

pi = PiRadians(F(1)).pi()


def test_pi_radians_from_radians():
    assert PiRadians.from_float_radians(math.pi) == PiRadians(F(1)) 
    assert PiRadians.from_float_radians(2*math.pi) == PiRadians(F(2)) 
    assert PiRadians.from_float_radians(F(3, 2)*math.pi) == PiRadians(F(3, 2)) 
    assert PiRadians.from_float_radians(math.pi/2) == PiRadians(F(1, 2)) 
    assert PiRadians.from_float_radians(math.pi/3) == PiRadians(F(1, 3)) 
    assert PiRadians.from_float_radians(math.pi/6) == PiRadians(F(1, 6)) 
    assert PiRadians.from_float_radians(math.pi/12) == PiRadians(F(1, 12)) 
    assert PiRadians.from_float_radians(3*math.pi/4) == PiRadians(F(3, 4)) 


def test_complex():
    assert atan(0) == 0
    z = complex(1, 0)
    assert angle(z) == PiRadians(F(0))
    assert PiRadians(F(1, 2)) == PiRadians(F(1)) / 2
    print(pi / 2)
    assert angle(complex(0, 1)) == pi / 2
    assert angle(complex(1, 1)) == PiRadians(F(1, 4))
    assert angle(complex(-1, 1)) == PiRadians(F(3, 4))
    assert angle(complex(4, 3)).error


def test_fraction():
    f = F('3.141592653589793')
    assert f.limit_denominator(10) == F(22, 7)
    assert f != F(22, 7)


def test_presentation():
    assert str(PiRadians(F(3, 2))) == "3π/2"
    assert str(PiRadians(F(2))) == "2π"
    assert str(PiRadians(F(-1))) == "-1π"
    assert str(PiRadians(F(1, 12))) == "π/12"
    assert PiRadians(F(1, 12)).__str__() == "π/12"
    assert PiRadians(F(1, 12)).__str__(F(2, 7)) == "2π/7"


def test_angle_change_based_on_complex():
    initial = angle(complex(2, 5))
    assert angle(complex(2, 5) * complex(0, 1)) - initial == pi / 2
    assert angle(complex(2, 5) * complex(0, 2)) - initial == pi / 2


def test_multiplication_of_complex_equals_sum_of_angles():
    assert angle(complex(3, 1) * complex(1, 3)) != pi / 3
    assert angle(complex(2, 1) * complex(1, 2)) == pi / 4 + pi / 4
    z = complex(4, 3)
    assert 2 * angle(z) == angle(z ** 2)
    z2 = complex(2, 3)
    assert angle(z * z2) == angle(z) + angle(z2)  # lika a logarithm


def test_dir():
    assert Magnitude.from_complex(complex(0, 0)) == 0
    assert Magnitude.from_complex(complex(0, 1)) == 1
    assert Magnitude.from_complex(complex(3, 4)) == 5


def test_arithmetic():
    a: int = 5

    assert type(a).__name__ == a.__class__.__name__ == "int"

    assert PiRadians(F(5, 4)) - PiRadians(F(1, 4)) == PiRadians(F(1))
    assert PiRadians(F(1))*2 == 2*PiRadians(F(1)) == PiRadians(F(2))
    assert isinstance(2, Real)
    assert isinstance(2, Integral)
    with pytest.raises(TypeError):
        PiRadians(F(1)) * PiRadians(F(1))

    assert PiRadians(F(2, 1)) / 3 == PiRadians(F(2, 3))
    assert pi*2/3 == PiRadians(F(2, 3))

    assert type(pi*2) == PiRadians
    assert PiRadians(F(4, 3)) - pi*2/3 == PiRadians(F(2, 3))
    assert PiRadians(F(1, 3)) + PiRadians(F(1, 2)) == PiRadians(F(5, 6))
    assert -PiRadians(F(1)) == PiRadians(F(-1))
class FiniteRoots():
    def __init__(self):
        self.roots = set()

    def add(self, element):
        self.roots.add(element)

    def __eq__(self, other):
        return self.roots == other

    @classmethod
    def square_root(cls, number):
        direct = math.sqrt(number)
        opposite = -direct
        roots = cls()
        roots.add(direct)
        roots.add(opposite)
        return roots

    def __mul__(self, other):
        roots = FiniteRoots()
        for i in self.roots:
            roots.add(i*other)
        return roots
# class Root:
#     def __init__(self):
#         pass
#
#     @classmethod


def test_composite_root():
    assert FiniteRoots.square_root(4) == {2, -2}
    assert FiniteRoots.square_root(4) * 2 == {4, -4}
    assert FiniteRoots.square_root(4) == FiniteRoots.square_root(4)
