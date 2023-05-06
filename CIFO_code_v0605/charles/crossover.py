from random import randint, uniform, sample
from charles.charles import  Individual #, Population


def single_point_co(p1, p2):
    co_point = randint(1, len(p1)-2)
    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]
    return Individual(representation=offspring1), Individual(representation=offspring2)


def uniform_co(p1, p2):
    offspring1 = []
    offspring2 = []
    for i in range(len(p1)):
        if uniform(0, 1) < 0.5:
            offspring1.append(p1[i])
            offspring2.append(p2[i])
        else:
            offspring1.append(p2[i])
            offspring2.append(p1[i])
    return Individual(representation=offspring1), Individual(representation=offspring2)

def multi_point_co(p1, p2, num_points=2):
    # Generate unique crossover points
    crossover_points = sorted(sample(range(1, len(p1)), num_points))

    offspring1 = []
    offspring2 = []

    # Iterate through the crossover points
    for i, point in enumerate(crossover_points):
        if i % 2 == 0:
            offspring1.extend(p1[:point] if i == 0 else p1[crossover_points[i - 1]:point])
            offspring2.extend(p2[:point] if i == 0 else p2[crossover_points[i - 1]:point])
        else:
            offspring1.extend(p2[:point] if i == 0 else p2[crossover_points[i - 1]:point])
            offspring2.extend(p1[:point] if i == 0 else p1[crossover_points[i - 1]:point])

    # Add the remaining parts of the parents
    offspring1.extend(p1[crossover_points[-1]:])
    offspring2.extend(p2[crossover_points[-1]:])

    return Individual(representation=offspring1), Individual(representation=offspring2)

if __name__ == '__main__':
    p1, p2 = [2, 7, 4, 3, 1, 5, 6, 9, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]
    o1, o2 = uniform_co(p1, p2)
    print(o1, o2)
