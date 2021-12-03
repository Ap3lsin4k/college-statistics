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
>>> # Zakolenko
  File "<stdin>", line 1
    ^ Zakolenko
    ^
SyntaxError: invalid syntax
>>> 3223 % 9 #: "Попенко Руслан"
1
"""
import os

inp = [
    4403,
    -1, -1,
    6403,
    3211,
    3110,
    8106,
    3308,
    2112,
    4120,
    7109,
    7218,
    3223,
    8121,
    -1,
    -1,
    3224,
    4126,
    -1,
    3330,
    2230,
    9204,
]


def eq(a, b, mod):
    return a % mod == b % mod


def test_listdir():
    my = 424
    div = 11
    # assert len(os.listdir("../resource")) > 5
    # assert os.listdir("../resource")
    # lastnames = sorted(os.listdir("../resource"))
    # print(lastnames)
    # d = dict(zip(inp, lastnames))

    # print(list(zip(inp, lastnames)))
    # for i in range(len(inp)):
        # val = lastnames[i]
        # print((inp[i], val))
        # if inp[i] == 3308:
        #     assert val == "Заколенко"
        # if inp[i] == 9204:
        #     assert val == "різні"

    # assert d[4126] == "Смішний Діма"
    # assert d[4403] == "Барабаш"
    # assert d[3224] == "Руденко"
    # assert d[3330] == "Шуркіна"
    # assert d[2230] == "Щербіна"

    assert eq(1, 5, 4)

    def myfilter(other):
        return eq(my, other[0], div)

    print("copy paste from: ")
    persons = [
        (4403, 'Барабаш'), (6403, 'Бровченко'), (3405, 'Власов'), (6403, 'Гаврилюк'), (3211, 'Довгаль'), (3110, 'Долинний'),
        (8106, 'Дудка'), (3308, 'Заколенко'), (2112, 'Коваленко'), (4120, 'Коноз'), (7109, 'Логвинчук'), (7218, 'Мазан'),
        (3223, 'Мироненко'), (8121, 'Наталка Д'), (3223, 'Попенко'), (8121, 'Рахуба'), (3224, 'Руденко'), (4126, 'Смішний Діма'),
        (7127, 'Чеботаренко'), (3330, 'Шуркіна'), (2230, 'Щербіна'), (9204, 'різні'), (424-11, 'Молочко'), (424-22, 'Водзінський'),
        (9322, 'danka'), (9201, 'Babenko'), (9319, 'IPZ new')
    ]

# list(zip(inp, lastnames))
    for person in filter(myfilter, persons):
        print(person, f"person.var % {div} = {person[0] % div}")
    print(list())


    # ls | xargs -i cat {} | pbcopy
    # find . | xargs -i cat {} | pbcopy
