from PopulationSandbox import models

POPULATION_SIZE = 1000000

my_pop = models.HumanGeneratorNoDistribution(population_size=POPULATION_SIZE)

for human in my_pop.get_filtered_population(f_name=('Sean', 'Kevin'), l_name=('Xie', 'Hess')):
    human.display_info()
