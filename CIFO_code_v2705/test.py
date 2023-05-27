from time import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from charles import Population, Individual
from sdp_data import data, min_nutrients, max_nutrients

from selection import fps
from mutation import random_mutation
from crossover import multi_point_co

results = pd.DataFrame(columns=['Penalty Size', 'Time Elapsed', 'Final Fitness', 'Final Cost',
                                'Number of Iterations', 'Final Quantity', 'Number of Requirements met'])

penalty_sizes = [10, 20, 50, 80, 100, 120]

fitness_values = []

for penalty_size in penalty_sizes:
    print("Penalty Size:", penalty_size)

    elite_fitness_values = []  # Store fitness values for each run

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
                penalty += nutrient_penalty * penalty_size  # Apply a penalty for each nutrient bellow requirement

        #max nutrients
        for i in range(len(max_nutrients)):
            if nutritional_values[i] > max_nutrients[i][1]:
                nutrient_range = max_nutrients[i][1] - min_nutrients[i][1]
                nutrient_penalty = (nutritional_values[i] - max_nutrients[i][1]) / nutrient_range
                penalty += nutrient_penalty * 5  # Apply a penalty for each nutrient above requirement

        return total_cost + penalty

    Individual.get_fitness = get_fitness  # Monkey patch the get_fitness method

    for _ in range(50):
        pop = Population(size=50,
                         optim="min",
                         sol_size=len(data),
                         valid_set=range(len(data)),
                         replacement=True)
        start_time = time()
        best_individual, fitness_history = pop.evolve(pop=pop,
                                                     generations=300,
                                                     select=fps,
                                                     mutate=random_mutation,
                                                     mutation_rate=0.5,
                                                     crossover=multi_point_co,
                                                     elite_size=2,
                                                     no_improvement_threshold=1000,
                                                     plot=None)
        end_time = time()

        # Initialize counts and metrics
        num_requirements_met = 0
        final_cost = 0
        nutritional_values = [0] * 15

        # Calculate nutritional values and other metrics
        for index, quantity in enumerate(best_individual.representation):
            for j in range(15):
                nutritional_values[j] += data[index][j + 2] * quantity

                if quantity > 0:
                    final_cost += data[index][1] * quantity

        for j, (nutrient, min_req) in enumerate(min_nutrients):
            if min_nutrients[j][1] <= nutritional_values[j] <= max_nutrients[j][1]:
                num_requirements_met += 1

        final_fitness = best_individual.get_fitness(penalty_size)  # Pass penalty_size to the get_fitness method
        num_iterations = len(fitness_history)
        final_qnt_ingredients = sum(best_individual.representation)

        # Append a row to the DataFrame
        row_data = {'Penalty Size': penalty_size,
                    'Time Elapsed': end_time - start_time,
                    'Final Fitness': final_fitness,
                    'Final Cost': final_cost,
                    'Number of Iterations': num_iterations,
                    'Final Quantity': final_qnt_ingredients,
                    'Number of Requirements met': num_requirements_met}

        results = pd.concat([results, pd.DataFrame(row_data, index=[0])], ignore_index=True)

        # Save fitness values at each iteration
        elite_fitness_values.append(fitness_history)

    fitness_values.append(elite_fitness_values)

print(results.head(5))
results.to_csv('results.csv', index=False)

# Calculate the mean fitness values for each penalty size
mean_fitness_values = [np.mean(fitness, axis=0) for fitness in fitness_values]
min_fitness_values = [np.min(fitness, axis=0) for fitness in fitness_values]
max_fitness_values = [np.max(fitness, axis=0) for fitness in fitness_values]

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the boxplots for each penalty size
sns.boxplot(x='Penalty Size', y='Final Fitness', data=results, ax=ax)

# Add mean, minimum, and maximum fitness values
for i, penalty_size in enumerate(penalty_sizes):
    ax.plot(np.arange(len(mean_fitness_values[i])) + 1, mean_fitness_values[i], label=f"Mean (Penalty Size: {penalty_size})")
    ax.plot(np.arange(len(min_fitness_values[i])) + 1, min_fitness_values[i], linestyle='--', alpha=0.5, label=f"Min (Penalty Size: {penalty_size})")
    ax.plot(np.arange(len(max_fitness_values[i])) + 1, max_fitness_values[i], linestyle='--', alpha=0.5, label=f"Max (Penalty Size: {penalty_size})")

# Set labels and title
ax.set_xlabel('Penalty Size')
ax.set_ylabel('Fitness')
ax.set_title('Boxplots of Fitness for Different Penalty Sizes')

# Add legend
ax.legend()

# Show the plot
plt.show()
