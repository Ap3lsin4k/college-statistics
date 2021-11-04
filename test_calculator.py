from fractions import Fraction


def test_g():
    from sympy.abc import i, k, m, n, x
    from sympy import Sum, factorial, oo, IndexedBase, Function
    # s = Sum((x+2)**k / (2**k * k**2), (k, 0, oo)).doit()
    s1 = Sum(x**k/k, (k, 1, oo)).doit()
    s2 = Sum(x**k/(k+1), (k, 1, oo)).doit()
    s2 = Sum(x**k/(k+1), (k, 1, oo)).doit()
    # assert s1 == s2 and False
    print()
    print(Sum(x**k/(k), (k, 1, oo)).doit())
    print(Sum(x**k/(k+1), (k, 1, oo)).doit())
    # print(Sum(x**k/(k+2), (k, 1, oo)).doit())
    # print(Sum(x**k/(k+3), (k, 1, oo)).doit())
    # print(Sum(x**k/(k+4), (k, 1, oo)).doit())
    assert s2 and False
