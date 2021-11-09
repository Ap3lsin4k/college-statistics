"""
6403,
3211,
3110,
8106,
3308,
2112 ,
4120,
7109,
7218,
3308,
>>> ^ Zakolenko
  File "<stdin>", line 1
    ^ Zakolenko
    ^
SyntaxError: invalid syntax
>>> 3223 % 9 : "Попенко Руслан"
1
"""
import os


inp = [
    -1,-1,-1,
    6403,
    3211,
    3110,
    8106,
    3308,
    2112 ,
    4120,
    7109,
    7218,
    3223,
    8121,
    -1,
    -1,
    4126,
    -1,
    9204,


]
def test_listdir():
    assert len(os.listdir("resource")) > 5
    assert os.listdir("resource")
    lastnames = sorted(os.listdir("resource"))
    print(lastnames)
    d = dict(zip(inp, lastnames))

    print(list(zip(inp, lastnames)))
    for i in range(len(inp)):
        val =lastnames [i]
        print([inp[i], val])
        if inp[i] == 3308:
            assert val == "Заколенко"
        if inp[i] == 9204:
            assert val == "різні"

    assert d[4126] == "Смішний Діма"
