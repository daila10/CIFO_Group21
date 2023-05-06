from charles.charles import Population, Individual
#from copy import deepcopy
from data.sdp_data import nutrients, data
from charles.selection import tournament_sel #,fps
from charles.mutation import binary_mutation
from charles.crossover import single_point_co
from random import randint, uniform, choice #,random
#from operator import attrgetter


def get_fitness(self):
    """A fitness function that returns the
    price of the food if it meets the requirements, otherwise the fitness is 2000.
    """
    total_cost = 0
    nutritional_values = [0] * 9  # Initialize nutritional values list with 0s

    for index in self.representation:
        total_cost += data[index][2]  # Accessing the price of the ingredient at the given index
        for i in range(9):
            nutritional_values[i] += data[index][i + 3]  # Accessing and accumulating nutritional values

    # Check if the requirements are met
    requirements_met = True
    for i, (nutrient, min_req) in enumerate(nutrients):
        if nutritional_values[i] < min_req:
            requirements_met = False
            break

    return total_cost if requirements_met else 2000

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


'''def get_neighbours(self):
    neighbours = []
    
    for i in range(7):  # Change the number of neighbours generated
        new_representation = self.representation.copy()
        
        change_type = uniform(0, 1)
        
        if change_type < 0.33:  # 33% chance to change one ingredient
            index_to_change = randint(0, len(self.representation) - 1)
            new_value = choice(range(len(data)))
            while new_value == self.representation[index_to_change]:
                new_value = choice(range(len(data)))
            new_representation[index_to_change] = new_value

        elif change_type < 0.66:  # 33% chance to add or remove an ingredient
            if uniform(0, 1) < 0.5:  # 50% chance to add a new ingredient
                new_ingredient = choice(range(len(data)))
                while new_ingredient in new_representation:
                    new_ingredient = choice(range(len(data)))
                new_representation.append(new_ingredient)
            else:  # 50% chance to remove an ingredient
                if len(new_representation) > 1:  # Check if there is any ingredient to remove
                    index_to_remove = randint(0, len(new_representation) - 1)
                    new_representation.pop(index_to_remove)
        
        else:  # 34% chance to change half the ingredients
            num_changes = len(new_representation) // 2
            for _ in range(num_changes):
                index_to_change = randint(0, len(new_representation) - 1)
                new_value = choice(range(len(data)))
                while new_value == self.representation[index_to_change]:
                    new_value = choice(range(len(data)))
                new_representation[index_to_change] = new_value
                
        neighbour = Individual(representation=new_representation)
        neighbours.append(neighbour)
    
    return neighbours'''


# Monkey Patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

pop = Population(size=10, optim="min", sol_size=len(data), valid_set=range(len(data)), replacement=True)

pop.evolve(gens=100, xo_prob=0.9, mut_prob=0.2, select=tournament_sel,
           mutate=binary_mutation, crossover=single_point_co,
           elitism=True)

