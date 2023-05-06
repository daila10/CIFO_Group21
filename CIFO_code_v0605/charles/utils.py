#import seaborn as sns
#import matplotlib.pyplot as plt
from copy import deepcopy
from data.sdp_data import nutrients, data


def fitness(number):
    #return "{0:04b}".format(number).count("1")
    return number**2

#print foods and its nutritional information
def print_nutrition(individual):
    total_cost = 0
    nutritional_values = [0] * 9 # Initialize nutritional values list with 0s
    ingredients = []

    for index in individual.representation:
        ingredients.append(data[index][0])  # Accessing the name of the ingredient at the given index
        total_cost += data[index][2]  # Accessing the price of the ingredient at the given index
        for i in range(9):
            nutritional_values[i] += data[index][i + 3]  # Accessing and accumulating nutritional values

    print(f"Total cost: {total_cost}")
    print(f"Number of ingredients chosen: {len(ingredients)}")
    print("Ingredients chosen: ", ingredients)
    for i, (nutrient, min_req) in enumerate(nutrients):
        print(f"{nutrient}: {nutritional_values[i]:.2f} ({min_req})")





