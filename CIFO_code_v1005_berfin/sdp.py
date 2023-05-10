
from charles import Population, Individual
#from copy import deepcopy
from sdp_data import data
from selection import tournament_selection #,fps
from mutation import food_combination_mutation
from crossover import single_point_co
from utils import plot_c
#from operator import attrgetter



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
get_neighbours = Individual.get_neighbours


