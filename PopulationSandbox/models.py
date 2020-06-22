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
        print(f'Name: {self.f_name} {self.l_name}')
        print(f'Age: {self.age} years')
        print(f'Occupation: {self.occupation}')

        print()


class Population:
    def __init__(self, size):
        self.size = size
        self.population = []

    # Filters
    def get_filtered_population(self, gender=(), f_name=(), l_name=(), age=()):
        print('here')
        filtered_pop = self.population

        if gender:
            filtered_pop = list(filter(lambda human: human.gender in gender, filtered_pop))

        if f_name:
            filtered_pop = list(filter(lambda human: human.f_name in f_name, filtered_pop))

        if l_name:
            filtered_pop = list(filter(lambda human: human.l_name in l_name, filtered_pop))

        if age:
            filtered_pop = list(filter(lambda human: human.age in age, filtered_pop))

        return filtered_pop

    def get_population(self):
        return self.population


class PopulationNoDistribution(Population):
    """An elementary model which has no weighted distributions"""

    def __init__(self, size):
        super().__init__(size)

    def calculate_population(self):
        for _ in range(self.size):
            gender = choice(['Male', 'Female'])  # Not very politically correct but give me a break
            age = randint(0, 100)

            self.population.append(
                Human(
                    gender=gender,

                    f_name=choice(data1.male_first_names) if gender == 'Male' else choice(data1.female_first_names),

                    l_name=choice(data1.surnames),

                    age=age,

                    occupation=choice(data1.occupations) if self.working_age <= age <= self.retirement_age else 'Unemployed'
                )
            )

    @property
    def working_age(self):
        return 21

    @property
    def retirement_age(self):
        return 65
