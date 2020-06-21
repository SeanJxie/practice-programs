from PopulationSandbox import tools

POPULATION_SIZE = 100

population = tools.human_generator(n=POPULATION_SIZE)

for human in population:
    human.display_info()
