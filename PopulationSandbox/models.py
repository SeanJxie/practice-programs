from PopulationSandbox.data_sets import data1
from random import choice, randint


class Human:
    def __init__(self, gender, f_name, l_name, age, occupation):
        self.gender = gender
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.occupation = occupation

    def display_info(self):
        print(f'Gender: {self.gender}')
        print(f'Name: {self.f_name + " " + self.l_name}')
        print(f'Age: {self.age}')
        print(f'Occupation: {self.occupation}')

        print()


def human_generator_no_distribution(n):
    """An elementary model which has no weighted distributions"""
    humans = []

    working_age = 16
    retirement_age = 65

    for _ in range(n):
        gender = choice(['Male', 'Female'])  # Not very politically correct but give me a break
        age = randint(0, 100)

        humans.append(
            Human(
                gender=gender,
                
                f_name=choice(data1.male_first_names) if gender == 'Male' else choice(data1.female_first_names),

                l_name=choice(data1.surnames),

                age=age,

                occupation=choice(data1.occupations) if working_age <= age <= retirement_age else 'Unemployed'
            )
        )

    return humans
