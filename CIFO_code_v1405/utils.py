#import seaborn as sns
import matplotlib.pyplot as plt
from sdp_data import nutrients, data
from collections import Counter

def fitness(number):
    #return "{0:04b}".format(number).count("1")
    return number**2

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
    for i, (nutrient, min_req) in enumerate(nutrients):
        print(f"{nutrient}: {nutritional_values[i]:.2f} ({min_req})")

    # Count the occurrences of each ingredient in the final solution
    ingredient_counts = Counter(ingredients)  # Use `ingredients` list instead of accessing data again

    # Print the ingredients and their counts in descending order
    print("\nIngredients chosen:")
    sorted_ingredient_counts = sorted(ingredient_counts.items(), key=lambda x: x[1], reverse=True)
    for ingredient, count in sorted_ingredient_counts:
        print(f"{ingredient}: {count}")

    print('')
    # Print the ingredients and their counts in descending order
    print("\nIngredients chosen:")
    sorted_ingredient_counts = sorted(ingredient_counts.items(), key=lambda x: x[1], reverse=True)
    print(", ".join(f"{ingredient}: {count}" for ingredient, count in sorted_ingredient_counts))

def plot_c(fitness_history_ga):
    plt.plot(fitness_history_ga)
    plt.title("Genetic Algorithm Fitness over Time")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.show()

def print_nutrition(individual):
    total_cost = 0
    nutritional_values = [0] * 9  # Initialize nutritional values list with 0s
    ingredients = []

    for index in individual.representation:
        ingredients.append(data[index][0])  # Accessing the name of the ingredient at the given index
        total_cost += data[index][1]  # Accessing the price of the ingredient at the given index
        for i in range(9):
            nutritional_values[i] += data[index][i + 2]  # Accessing and accumulating nutritional values

    print(f"Total cost: {total_cost}")
    print(f"Number of ingredients chosen: {len(ingredients)}")
    print("Ingredients chosen: ", ingredients)
    for i, (nutrient, min_req) in enumerate(nutrients):
        print(f"{nutrient}: {nutritional_values[i]:.2f} ({min_req})")

