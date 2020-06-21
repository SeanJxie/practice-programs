from PopulationSandbox import data
from random import choice, randint


class Human:
    def __init__(self, f_name, l_name, age, occupation):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.occupation = occupation

    def display_info(self):
        print(f'Name: {self.f_name + " " + self.l_name}')
        print(f'Age: {self.age}')
        print(f'Occupation: {self.occupation}')

        print()


def human_generator(n):
    """An elementary model which has no weighted distributions"""
    humans = []

    for _ in range(n):
        humans.append(
            Human(
                f_name=choice([choice(data.male_first_names), choice(data.female_first_names)]),
                l_name=choice(data.surnames),
                age=randint(0, 100),
                occupation=choice(data.occupations)
            )
        )

    return humans
