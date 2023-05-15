from sdp_data import nutrients, data
from random import randint, uniform, choice
from charles import Population, Individual
from selection import tournament_selection #,fps
from mutation import random_mutation
from crossover import single_point_co
from utils import plot_c

def get_fitness(self):
    """A fitness function that returns the
    price of the food if it meets the requirements, otherwise the fitness gets a penalty
    """
    total_cost = 0
    nutritional_values = [0] * 15  # Initialize nutritional values list with 0s

    for index, quantity in enumerate(self.representation):
        total_cost += quantity * data[index][2]  # Accessing the price of the ingredient at the given index
        for i in range(15):
            nutritional_values[i] +=quantity + data[index][i + 2]  # Accessing and accumulating nutritional values

    # Calculate penalty for not meeting the nutritional requirements
    penalty = 0
    for i in range(len(nutrients)):
        if nutritional_values[i] < nutrients[i][1]:
            penalty += (nutrients[i][1] - nutritional_values[i]) * 100  # Apply a penalty for each nutrient not met

    return total_cost + penalty

# Monkey Patching
Individual.get_fitness = get_fitness

pop = Population(size=20, optim="min", sol_size=len(data), valid_set=range(len(data)), replacement=True)

pop.evolve(pop=pop, generations=1000, select=tournament_selection,
           mutate=random_mutation, mutation_rate=0.4, crossover=single_point_co,
           elite_size=2, no_improvement_threshold=100, plot= plot_c)