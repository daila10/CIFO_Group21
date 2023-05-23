import matplotlib.pyplot as plt
from sdp_data import min_nutrients, max_nutrients, data
from charles import Population, Individual
from selection import tournament_selection, ranking_selection ,fps
from mutation import random_mutation, geometric_mutation, insert_delete_mutation
from crossover import single_point_co, uniform_co, multi_point_co, arithmetic_co, geometric_co, cycle_xo, pmx
from utils import plot_c

def get_fitness(self):
    """A fitness function that returns the
    price of the food if it meets the requirements, otherwise the fitness gets a penalty
    """
    total_cost = 0
    nutritional_values = [0] * 15  # Initialize nutritional values list with 0s

    for index, quantity in enumerate(self.representation):
        total_cost += quantity * data[index][1]  # Accessing the price of the ingredient at the given index
        for i in range(15):
            nutritional_values[i] +=quantity + data[index][i + 2]  # Accessing and accumulating nutritional values

    # Calculate penalty for not meeting the nutritional requirements

    penalty = 0

    #min nutrients
    for i in range(len(min_nutrients)):
        if nutritional_values[i] < min_nutrients[i][1]:
            nutrient_range = max_nutrients[i][1] - min_nutrients[i][1]
            nutrient_penalty = (min_nutrients[i][1] - nutritional_values[i]) / nutrient_range
            penalty += nutrient_penalty * 20  # Apply a penalty for each nutrient bellow requirement

    #max nutrients
    for i in range(len(max_nutrients)):
        if nutritional_values[i] > max_nutrients[i][1]:
            nutrient_range = max_nutrients[i][1] - min_nutrients[i][1]
            nutrient_penalty = (nutritional_values[i] - max_nutrients[i][1]) / nutrient_range
            penalty += nutrient_penalty * 5  # Apply a penalty for each nutrient above requirement

    return total_cost + penalty

# Monkey Patching
Individual.get_fitness = get_fitness


## -------- code to run alg one time ---------- ##

'''pop = Population(size=50,
                 optim="min",
                 sol_size=len(data),
                 valid_set=range(len(data)),
                 replacement=True)

pop.evolve(pop=pop,
           generations=100,
           select=fps,
           mutate= geometric_mutation,
           mutation_rate=0.5,
           crossover= pmx,
           elite_size=2,
           no_improvement_threshold=50,
           plot= plot_c)'''


## -------- code to run alg with multiple combinations ---------- ##




'''# Define the combinations of select methods, mutation operators, and crossover operators
select_methods = [tournament_selection, ranking_selection ,fps]
mutation_operators = [random_mutation, geometric_mutation, insert_delete_mutation]
crossover_operators = [single_point_co, uniform_co, multi_point_co, arithmetic_co, geometric_co]

# Create empty lists to store results and plots
combinations = []
results = []
plots = []

# Iterate over the combinations
for select_method in select_methods:
    for mutation_operator in mutation_operators:
        for crossover_operator in crossover_operators:

            #save name of the current operators
            combination = [f"{select_method}", f"{mutation_operator}", f"{crossover_operator}"]
            one_combination_results = []
            one_combination_plots = []

            #run one combination 30 times
            for _ in range(30):
                pop = Population(size=10, optim="min", sol_size=len(data), valid_set=range(len(data)), replacement=True)
                # Run the algorithm for each combination and store result
                one_combination_results.append(pop.evolve(pop=pop, generations=1000, select=select_method,
                        mutate=mutation_operator, mutation_rate=0.2, crossover=crossover_operator,
                        elite_size=2, no_improvement_threshold=100, plot=plot_c)[0])
                
                # Store the  and plots
                one_combination_plots.append(plt.gcf())

                plt.clf()  # Clear the plot for the next iteration

            combinations.append(combination)
            results.append(one_combination_results)
            plots.append(one_combination_plots)

#save results'''