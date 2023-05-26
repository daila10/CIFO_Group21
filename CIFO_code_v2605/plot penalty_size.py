from time import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from charles import Population, Individual
from sdp_data import data, min_nutrients, max_nutrients
from sdp_run import get_fitness

from selection import fps
from mutation import random_mutation
from crossover import multi_point_co

results = pd.DataFrame(columns=['Penalty Size', 'Time Elapsed', 'Final Fitness', 'Final Cost',
                                'Number of Iterations', 'Final Quantity', 'Number of Requirements met'])

penalty_sizes = [10, 20, 50, 80, 100, 120]

#Individual.get_fitness = get_fitness(penalty_size=20)

fitness_values = []

for penalty in penalty_sizes:
    print("Elite Size:", penalty)
    elite_fitness_values = []  # Store fitness values for each run
    Individual.get_fitness = get_fitness(self, penalty_size=penalty)
    for _ in range(3):
        pop = Population(size=10,
                         optim="min",
                         sol_size=len(data),
                         valid_set=range(len(data)),
                         replacement=True)
        start_time = time()
        best_individual, fitness_history = pop.evolve(pop=pop,
                                                     generations=10,
                                                     select=fps,
                                                     mutate=random_mutation,
                                                     mutation_rate=0.5,
                                                     crossover=multi_point_co,
                                                     elite_size=8,
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

        final_fitness = best_individual.get_fitness()
        num_iterations = len(fitness_history)
        final_qnt_ingredients = sum(best_individual.representation)

        # Append a row to the DataFrame
        row_data = {'Penalty Size': penalty,
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

# Calculate the mean fitness values for each elite size
mean_fitness_values = [np.mean(fitness, axis=0) for fitness in fitness_values]
min_fitness_values = [np.min(fitness, axis=0) for fitness in fitness_values]
max_fitness_values = [np.max(fitness, axis=0) for fitness in fitness_values]

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the line chart for each elite size
for i, elite_size in enumerate(penalty_sizes):
    ax.plot(range(len(mean_fitness_values[i])), mean_fitness_values[i], label=f'Penalty Size {elite_size}')
    ax.fill_between(range(len(mean_fitness_values[i])), min_fitness_values[i], max_fitness_values[i], alpha=0.3)

# Set the x-axis label
ax.set_xlabel('Generations')

# Set the y-axis label
ax.set_ylabel('Mean Best Fitness')

# Set the title
ax.set_title('Mean Best Fitness Progression for Different Penalty Sizes')

# Add a legend
ax.legend()

# Show the plot
plt.show()
