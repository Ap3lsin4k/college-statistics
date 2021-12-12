import math


def how_many_integer_multiple_in_interval(a, b, c):
    a = a - (a % c) + (c if a % c else 0)
    return calc(a, b - (b % c) + c, c)

def calc(a, b, c):
    return (b-a) / c


def solve(a, b, c, d):
    return (b - a + 1) - how_many_integer_multiple_in_interval(a, b, c) - how_many_integer_multiple_in_interval(a, b, d) \
           + how_many_integer_multiple_in_interval(a, b, math.lcm(c, d))

def test_prime():
    stdin = "4 9 2 3"
    a, b, c, d = map(int, stdin.split())

    assert how_many_integer_multiple_in_interval(0, 0, c=1) == 1
    assert how_many_integer_multiple_in_interval(0, 3, c=3) == 2
    assert how_many_integer_multiple_in_interval(a=2, b=4, c=2) == 2

    assert how_many_integer_multiple_in_interval(1, 2, 2) == 1
    assert how_many_integer_multiple_in_interval(1, 3, 2) == 1
    assert how_many_integer_multiple_in_interval(1, 4, 2) == 2
    assert how_many_integer_multiple_in_interval(1, 1, 2) == 0
    assert how_many_integer_multiple_in_interval(0, 4, 3) == 2
    assert how_many_integer_multiple_in_interval(0, 5, 3) == 2
    assert how_many_integer_multiple_in_interval(1, 5, 3) == 1
    assert how_many_integer_multiple_in_interval(2, 5, 3) == 1

def test_solve():
    assert how_many_integer_multiple_in_interval(4, 9, 2) == 3
    assert how_many_integer_multiple_in_interval(4, 9, 3) == 2
    assert how_many_integer_multiple_in_interval(4, 9, 6) == 1

    assert solve(4, 9, 2, 3) == 9 - 4+ 1 - 3- 2 +1 == 2
    stdin = "4 9 2 3"
    a, b, c, d = map(int, stdin.split())
    assert solve(a, b, c, d) == 2
    assert how_many_integer_multiple_in_interval(10, 40, 8) == 4
    assert how_many_integer_multiple_in_interval(0, 40-12, 6) == len({12, 18, 24, 30, 36}) == 5

    assert how_many_integer_multiple_in_interval(6+6, 40, 6) == len({12, 18, 24, 30, 36}) == 5
    assert how_many_integer_multiple_in_interval(10, 40, 6) == len({12, 18, 24, 30, 36}) == 5
    assert how_many_integer_multiple_in_interval(10, 40, (3*2)*4) == 1
    assert len({10, 11, 13, 14, 15, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 31, 33, 34, 35, 37, 38, 39}) == 23
    assert 31 - len({12, 16, 18, 24, 30, 32, 36, 40}) == 23
    assert len({12, 16, 18, 24, 30, 32, 36, 40}) == 8
    assert len({12, 18, 24, 30, 36, 40}) == 6  # number of 6 submultipliers
    assert len({16, 24, 32, 40}) == 4
    assert -6-4+2 == -8


    # assert 0, {i for i in range(16, 40 + 1, 8)} | {i for i in range(12, 40 + 1, 6)}
    #
    # assert 0, {i for i in range(16, 40+1, 8)}.intersection({i for i in range(12, 40+1, 6)})
    # assert 30 - 1 - 5 - 4 - 1 == 23

    # assert solve(10, 40, 6, 8) == 30 + 1 - 5 - 4
    # 40-10 +1 -



