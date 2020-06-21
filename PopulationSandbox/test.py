from PopulationSandbox import models

POPULATION_SIZE = 1000000

population = models.HumanGeneratorNoDistribution(population_size=POPULATION_SIZE)


for human in population.get_population():
    human.display_info()
