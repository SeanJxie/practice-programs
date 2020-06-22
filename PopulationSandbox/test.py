from PopulationSandbox import models

POPULATION_SIZE = 1000000

my_pop = models.PopulationNoDistribution(size=POPULATION_SIZE)

my_pop.calculate_population()

for human in my_pop.get_filtered_population(gender='Male'):
    human.display_info()
