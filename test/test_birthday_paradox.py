import random
from time import sleep

import pytest
from fractions import Fraction





def present_experiment(experiments, group_size, shared):
    print(f"End of simulation. \nIn {shared} groups, people share birthday.")
    # sleep(0.8)
    print(f"In {experiments - shared} groups, people do not share birthday.")
    # sleep(0.8)
    print(f"\nChance of a shared birthday for a group of {group_size} people:")
    print(f"\tExperimental - {shared / experiments * 100}%")
    print(f"\tTheoretical - 70.6%")


class Person(int):
    def __new__(cls, birthday):
        if 1 <= birthday <= 365:
            return super(Person, cls).__new__(cls, birthday)
        else:
            raise ValueError


class Group:
    def __init__(self, persons):
        self.persons = persons
        self.unique_birthdays = len(set(self.persons))

    @property
    def shared_birthday(self):
        return len(set(self.persons)) != len(self.persons)

    @property
    def how_many_people_share_birthday(self):
        return len(self.persons) - self.unique_birthdays


def run_simulation(groups, people_in_a_group=30):
    print(f"\n\nStarting simulation with {people_in_a_group} people in a group...")
    for i in range(groups):
        group = RandomGroup(people_in_a_group)

        print(f"group #{i}, {len(set(group.persons))} unique birthdays out of {people_in_a_group}")

        yield group.shared_birthday


def test_random():
    random_range = random.randint(1, 4)
    assert 4 == random_range \
        or 1 == random_range \
        or 2 == random_range \
        or 3 == random_range
    number_of_people_in_a_group: int = 23


def test_person_init():
    Person(1)
    with pytest.raises(Exception):
        Person(367)
    with pytest.raises(Exception):
        Person(0)


def test_person():
    assert len({Person(1), Person(1)}) == 1
    assert len({Person(1), Person(2)}) == 2
    assert len({Person(365), Person(365)}) == 1
    assert int(Group(persons=(Person(1), Person(1))).shared_birthday) == 1
    assert int(Group(persons=(Person(1), Person(2))).shared_birthday) == 0
    assert Group(
        persons=(Person(1), Person(1), Person(1))
    ).how_many_people_share_birthday == 3
    assert Group(
        persons=(Person(1), Person(1), Person(2), Person(2))
    ).how_many_people_share_birthday == 2


def test_group():
    Group(persons=(Person(1), Person(1)))


class RandomGroup(Group):
    def __init__(self, num_of_people):
        super().__init__([Person(birthday=random.randint(1, 4)) for _ in range(num_of_people)])
        self.num_of_people = num_of_people


def test_birthday_paradox():
    experiments = 8000
    group_size = 3
    theoretical_chance_of_shared_birthday = 0.706
    shared = 0
    for does_group_share_birthday in run_simulation(experiments, group_size):
        if does_group_share_birthday:
            shared += 1  # print(f"{does_group_share_birthday+1} people share birthday")  # else:  #     print(f"no people share birthday")
    present_experiment(experiments, group_size, shared)
    return shared


def test_fraction_multiplier():
    assert Fraction(3/4)*Fraction(2/4) == Fraction(3/8)