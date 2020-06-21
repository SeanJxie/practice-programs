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


class HumanGeneratorNoDistribution:
    """An elementary model which has no weighted distributions"""

    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []

        for _ in range(self.population_size):
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

    def get_population(self):
        return self.population

    # Filters
    def filter_population_by_full_name(self, f_name, l_name):
        filtered_pop = []

        for human in self.population:
            if human.f_name == f_name and human.l_name == l_name:
                filtered_pop.append(human)

        return filtered_pop

    def filter_population_by_f_name(self, name):
        filtered_pop = []

        for human in self.population:
            if human.f_name == name:
                filtered_pop.append(human)

        return filtered_pop

    def filter_population_by_l_name(self, name):
        filtered_pop = []

        for human in self.population:
            if human.l_name == name:
                filtered_pop.append(human)

        return filtered_pop

    def filter_population_by_age(self, age):
        filtered_pop = []

        for human in self.population:
            if human.age == age:
                filtered_pop.append(human)

        return filtered_pop

    def filter_population_by_employment(self):
        filtered_pop = []

        for human in self.population:
            if human.occupation != 'Unemployed':
                filtered_pop.append(human)

        return filtered_pop

    @property
    def working_age(self):
        return 21

    @property
    def retirement_age(self):
        return 65
