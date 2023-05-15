from sdp_data import nutrients, data
from random import randint, uniform, choice
from charles import Population, Individual
from selection import tournament_selection #,fps
from mutation import food_combination_mutation, variable_size_mutation
from crossover import single_point_co
from utils import plot_c


def get_fitness(self):
    """A fitness function that returns the
    price of the food if it meets the requirements, otherwise the fitness is 2000.
    """
    total_cost = 0
    nutritional_values = [0] * 15  # Initialize nutritional values list with 0s

    for index in self.representation:
        total_cost += data[index][1]  # Accessing the price of the ingredient at the given index
        for i in range(10):
            nutritional_values[i] += data[index][i + 1]  # Accessing and accumulating nutritional values

    # Calculate penalty for not meeting the nutritional requirements
    penalty = 0
    for i in range(len(nutrients)):
        if nutritional_values[i] < nutrients[i][1]:
            penalty += (nutrients[i][1] - nutritional_values[i]) * 100  # Apply a penalty for each nutrient not met

    return total_cost + penalty


def get_neighbours(self):
    neighbours = []
    
    for i in range(7):  # Change the number of neighbours generated
        new_representation = self.representation.copy()
        index_to_change = randint(0, len(self.representation) - 1)
        new_value = choice(range(len(data)))
        while new_value == self.representation[index_to_change]:
            new_value = choice(range(len(data)))
        new_representation[index_to_change] = new_value
        
        if uniform(0, 1) < 0.5:  # 50% chance to add a new ingredient
            new_ingredient = choice(range(len(data)))
            while new_ingredient in new_representation:
                new_ingredient = choice(range(len(data)))
            new_representation.append(new_ingredient)
        else:  # 50% chance to remove an ingredient
            if len(new_representation) > 1:  # Check if there is any ingredient to remove
                index_to_remove = randint(0, len(new_representation) - 1)
                new_representation.pop(index_to_remove)
            
        neighbour = Individual(representation=new_representation)
        neighbours.append(neighbour)
    
    return neighbours

# Monkey Patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

pop = Population(size=20, optim="min", sol_size=len(data), valid_set=range(len(data)), replacement=True)

pop.evolve(pop=pop, generations=1000, select=tournament_selection,
           mutate=variable_size_mutation, mutation_rate=0.4, crossover=single_point_co,
           elite_size=2, no_improvement_threshold=100, plot= plot_c)