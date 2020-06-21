from PopulationSandbox import models

POPULATION_SIZE = 100

population = models.human_generator_no_distribution(n=POPULATION_SIZE)

for human in population:
    human.display_info()
