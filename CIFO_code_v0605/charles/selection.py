from random import uniform, choice, choices, sample
from operator import attrgetter

def fps(population):
    total_fitness = sum([i.fitness for i in population])
    spin = uniform(0, total_fitness)
    position = 0
    for individual in population:
        position += individual.fitness
        if position > spin:
            return individual

def ranking_selection(population):
    sorted_pop = sorted(population, key=lambda x: x.fitness)
    fitness_sum = sum(i for i in range(1, len(population) + 1))
    probabilities = [i/fitness_sum for i in range(1, len(population) + 1)]
    chosen = choices(sorted_pop, weights=probabilities, k=2)
    return chosen[0], chosen[1]


def tournament_selection(population, tournament_size=2):
    participants = sample(list(population), tournament_size)
    winner = min(participants, key=lambda x: x.fitness)
    return winner

