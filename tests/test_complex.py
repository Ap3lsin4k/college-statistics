import math
from fractions import Fraction as F
from math import atan

import pytest

from src.rotation import PiRadians


def angle(z: complex):
    try:
        return PiRadians.from_float_radians(math.atan2(z.imag, z.real))
    except ZeroDivisionError:
        return PiRadians(F(1, 2))


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


def test_multiply():
    initial = angle(complex(2, 5))
    assert angle(complex(2, 5)*complex(0, 1)) - initial == PiRadians(F(1, 2))


def test_arithmetic():
    assert PiRadians(F(5, 4)) - PiRadians(F(1, 4)) == PiRadians(F(1))
    assert PiRadians(F(1))*2
    assert 2*PiRadians(F(1))
#    assert pi*2 ==
    #2*pi
    assert PiRadians(F(4, 3)) - pi*2/3 == PiRadians(F(2, 3))