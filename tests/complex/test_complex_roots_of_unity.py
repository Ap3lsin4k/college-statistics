import sympy as sym
from IPython.display import display, Math


def test_complex():

    def roots(n=5):
        for k in range(n):
            yield sym.exp(2 * sym.pi * sym.I * k / n) ** n
    # assert 0, [ for k in range(n)
        # root =

    n = 4
    for z in roots(4):
        display(Math(f"{sym.latex(z)}^{n} \\Rightarrow {sym.latex(z**n)}"))
