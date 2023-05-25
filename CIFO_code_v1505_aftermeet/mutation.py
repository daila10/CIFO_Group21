from random import randint, choice
from sdp_data import data

def food_combination_mutation(individual):
    mut_index = randint(0, len(individual) - 1)
    new_value = choice(range(len(data)))
    while new_value == individual[mut_index]:
        new_value = choice(range(len(data)))
    individual[mut_index] = new_value
    return individual

def variable_size_mutation(individual):
    operation = choice(["add", "remove", "change"])

    if operation == "add":
        ingredient_to_add = choice(range(len(data)))
        individual.append(ingredient_to_add)

    elif operation == "remove" and len(individual) > 1:
        ingredient_to_remove = choice(individual)
        individual.remove(ingredient_to_remove)

    elif operation == "change":
        mut_index = randint(0, len(individual) - 1)
        new_value = choice(range(len(data)))
        while new_value == individual[mut_index]:
            new_value = choice(range(len(data)))
        individual[mut_index] = new_value

    return individual