import math

import pytest
from fractions import Fraction


class Series:
    infinity = 100

    def __init__(self, a=lambda n: Fraction(), seq=None, infinity_power=3):
        self.a = a
        self.value = sum([self.a(n) for n in range(1, 10 ** infinity_power)])

        self.diverges = self.value == float('inf')

    def __eq__(self, other):
        return pytest.approx(self.value, 0.1) == other

    def __repr__(self):
        return str(float(self.value))

    def __str__(self):
        return repr(self)+" = "+" + ".join(map(str, [self.a(n) for n in range(1, 10)])) + " + ..."

    def __iter__(self):
        self.elem_index = 0
        return self

    def __next__(self):
        self.elem_index += 1
        return self.a(self.elem_index)


def test_series():
    s = Series(lambda n: Fraction(1, 2 ** n))
    assert s == s

    assert s == 1

    assert not s.diverges


def test_natural_num():
    natural = Series(lambda n: n)
    natural_num_sequence = iter(natural)
    assert next(natural_num_sequence) == 1
    assert next(natural_num_sequence) == 2
    assert next(natural_num_sequence) == 3
    assert next(natural_num_sequence) == 4


def test_element_of_series():
    problem_1_5 = Series(lambda n: Fraction(n, 2 ** n * (n + 1)))
    iter(problem_1_5)
    next(problem_1_5)  # 1
    next(problem_1_5)
    next(problem_1_5)
    next(problem_1_5)
    next(problem_1_5)  # 5
    next(problem_1_5)
    next(problem_1_5)
    next(problem_1_5)  # 8
    next(problem_1_5)
    assert next(problem_1_5) == problem_1_5.a(10)


def test_problem_1_5_2():
    problem_1_5_2 = Series(lambda n: Fraction(3 ** n, math.factorial(n)))
    problem_1_5_2 = iter(problem_1_5_2)
    assert next(problem_1_5_2) == 3
    assert next(problem_1_5_2) == 9 / 2
    assert next(problem_1_5_2) == 27 / 6


class LogicSeries:
    def __init__(self, *args):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return "1/7*5"


@pytest.mark.skip("not implemented")
def test_logical_guess():
    l = LogicSeries("1/1*3", "1/3*5", "1/5*7")
    iter(l)
    next(l)
    next(l)
    next(l)
    assert str(next(l)) == "1/7*5"


class PartialSum:
    def __init__(self, finite_sum):
        def a(n):
            if n < 1:
                raise ValueError("Indexing starts from 1")
            if n == 1:
                return finite_sum(1)
            else:
                return finite_sum(n) - finite_sum(n - 1)

        self.a = a

        self.series = None  # Series(finite_sum)
    #
    # def a(self, param):
    #     pass


def test_partial_sum():
    def partial_sum(num_of_elems):
        n = num_of_elems  # in a sum
        return Fraction(n * (n + 3), 4 * (n + 1) * (n + 2))

    part_sum = PartialSum(partial_sum)
    assert part_sum.a(1) == Fraction(1, 1 * 2 * 3)
    assert part_sum.series != Series(lambda n: Fraction(n * (n + 3), 4 * (n + 1) * (n + 2)))
    assert Fraction(5, 2 * 2 * 2 * 3) - Fraction(4, 24) == part_sum.a(2)
    assert Fraction(1, 3 * (3 + 1) * (3 + 2)) == part_sum.a(3)
    assert Fraction(1, 4 * 2 * 3 * 5) == part_sum.a(4)
    assert Fraction(1, (lambda n: n * (n + 1) * (n + 2))(5)) == part_sum.a(5)
    assert Fraction(1, (lambda n: n * (n + 1) * (n + 2))(6)) == part_sum.a(6)

    with pytest.raises(ValueError):
        part_sum.a(0)

    for n in range(6, 10):
        assert part_sum.a(n) == partial_sum(n) - partial_sum(n - 1)
        assert part_sum.a(n) == Fraction(n * (n + 3), 4 * (n + 1) * (n + 2)) - Fraction((n - 1) * ((n - 1) + 3),
                                                                                        4 * ((n - 1) + 1) * (
                                                                                                (n - 1) + 2))
        assert part_sum.a(n) != Fraction(n * (n + 3) - (n - 1) * ((n - 1) + 3),
                                         4 * (n + 1) * (n + 2) - 4 * ((n - 1) + 1) * ((n - 1) + 2))
    # assert partial_sum(3) ==


class InfiniteSeq:
    def __init__(self, a):
        pass


def test():
    seq = InfiniteSeq(lambda n: Fraction(n * (n + 3), 4 * (n + 1) * (n + 2)))
    series = Series(seq=seq)


# noinspection PyTypeChecker
@pytest.mark.skip("Slow")
def test_term_paper_1_2():
    # a = Series(lambda n: math.log(n)/math.sqrt(n**8+n), infinity_power=6)
    assert Series(lambda n: math.log(n) / math.sqrt(n ** 8 + n), infinity_power=1) == Series(
        lambda n: math.log(n) / math.sqrt(n ** 8 + n), infinity_power=3)
    print(3 / 43)
    # assert  == 20.20


# noinspection PyTypeChecker
@pytest.mark.skip("Slow")
def test_term_paper_1_3():
    a = Series(lambda n: math.sin(math.sqrt(n) / math.sqrt(n ** 5 + 2)), infinity_power=8)
    print(a)
    assert a == 1.18


def test_khan_academy_college_calculus_conv_div():
    a = lambda n: Fraction(5 ** (2 * n), 4 ** (3 * n))
    s = Series(a, infinity_power=1)
    print(s)
    print(repr(s))
    assert s == Series(a, infinity_power=2)
    print(repr(s), repr(Series(a, infinity_power=2)))


def test_c():
    n = 2
    assert math.log(n)/n*n > Fraction(1, n*n)


# def test_a():
#     def a(n):
#         return (x+1)**n /(n+1)**(Fraction(1, 3))
#     for i in range(10):
#         x = 0.35*i-2
#         s1 = Series(a, infinity_power=2)
#         s2 = Series(a, infinity_power=3)
#         print(x, "\t", s1)
#         assert s1 == s2
#

def test_func_of_x():
    def a(n):
        return (x+2)**n / (2**n * n**2)
    for i in range(10):
        x = i*0.45 - 4
        s1 = Series(a, infinity_power=2)
        s2 = Series(a, infinity_power=3)
        print("\t", s1)
        assert s1 == s2
