import math
from fractions import Fraction

from sympy import limit
from sympy.plotting.intervalmath import cos


def test_g():
    from sympy.abc import i, k, m, n, x
    from sympy import pi, cos
    from sympy import Sum, factorial, oo, IndexedBase, Function
    # s = Sum((x+2)**k / (2**k * k**2), (k, 0, oo)).doit()
    # 1-1+cos = 1-(1-cos)=
    s1 = Sum(
        (1-(pi*k)**2/2) / (3**k*(k+1)),
        (k, 1, oo)).doit()
    assert s1


M = 1


def test_error_bound():
    x = 0.4
    e = 1e-3
    n = 1
    while x**(n+1)/math.factorial(n) > e:
        n += 1
    assert x**(n+1)/math.factorial(n) < e
    print(f"n:{n}\t{x**(n+1)/math.factorial(n)}")
    print(f"n:{n-1}\t{x**(n)/math.factorial(n-1)}")


def test_mkr():
    from sympy.abc import i, k, m, n, x
    from sympy import pi, cos
    from sympy import Sum, factorial, oo, IndexedBase, Function
    # s = Sum((x+2)**k / (2**k * k**2), (k, 0, oo)).doit()
    # 1-1+cos = 1-(1-cos)=
    # s1 = Sum(
    #     ((-1)**k * 12**k * 4)
    #     / (factorial(k) * 10 ** (2*k+1) * (2*k + 1)),
    #     (k, 0, oo)).doit()

    s2 = Sum(
        ((-1)**k)
        * (3/4) ** k
        * ((2/5) ** (2*k + 1))
        / (2*k+1),
        (k, 0, oo)).doit()
    assert s2 and False

