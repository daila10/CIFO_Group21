#import seaborn as sns
import matplotlib.pyplot as plt
from sdp_data import nutrients, data

def fitness(number):
    #return "{0:04b}".format(number).count("1")
    return number**2

def plot_c(fitness_history_ga):
    plt.plot(fitness_history_ga)
    plt.title("Genetic Algorithm Fitness over Time")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.show()

def print_nutrition(individual):
    total_cost = 0
    nutritional_values = [0] * 15  # Initialize nutritional values list with 0s
    ingredients = []

    for index, quantity in enumerate(individual.representation):
        if quantity > 0:
            ingredients.append([data[index][0], quantity])  # Accessing the name of the ingredient at the given index
            total_cost += data[index][1] * quantity # Accessing the price of the ingredient at the given index
            for i in range(15):
                nutritional_values[i] += data[index][i + 2] * quantity  # Accessing and accumulating nutritional values

    print(f"Total cost: {total_cost}")
    print(f"Number of ingredients chosen: {len(ingredients)}")
    for i, (nutrient, min_req) in enumerate(nutrients):
        print(f"{nutrient}: {nutritional_values[i]:.2f} ({min_req})")

    # Print the ingredients and their counts in descending order
    print("\nIngredients chosen:")
    for ingredient, quantity in ingredients:
        print(f"{ingredient}: {quantity}")

    print('')
    # Print the ingredients and their counts in descending order
    print("\nIngredients chosen:")
    print(", ".join(f"{ingredient}: {count}" for ingredient, count in ingredient))


