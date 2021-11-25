import math

import pytest



def test_e():
    lambd = 1./10**5
    chance_one_computer_works_two_years_sraight = math.e**(-lambd*10400)
    print(chance_one_computer_works_two_years_sraight)
    assert 0.9012252974212048 == pytest.approx(chance_one_computer_works_two_years_sraight)


    # def puason_bernolli(success, failure):
    #     assert 0 <= success <= 100 # num of computer
    #     assert success + failure == 100
        # return

    n = 100
    s = 0
    for k in range(95):
        s += math.factorial(n)/(math.factorial(k)*(math.factorial(n-k))) * (chance_one_computer_works_two_years_sraight ** k) * (
                1 - chance_one_computer_works_two_years_sraight) ** (n-k)
    print(s)
    # print(sum([puason_bernolli(100-i, i) for i in range(101)]))
        # print(f"probability {i} blocks failed: ", )

def test_e3():
    chance_one_block_does_not_two_years_sraight = 1 - 0.9012252974212048
