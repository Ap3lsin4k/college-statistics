from fractions import Fraction

import numpy as np


def a(n):
    return Fraction(1, n)


infinity_power=3

def test_benchmark_np(benchmark):
    def npsum():
        np.sum((a(n) for n in range(1, 10 ** infinity_power)))
    benchmark(npsum)

def test_benchmark_sum_built_in(benchmark):
    def mysum():
        sum((a(n) for n in range(1, 10 ** infinity_power)))
    benchmark(mysum)



