from random import randint, uniform, sample, random

def single_point_co(p1, p2):
    co_point = randint(1, len(p1)-2)
    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]
    return offspring1, offspring2

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
    return offspring1, offspring2

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

    return offspring1, offspring2

def arithmetic_co(p1, p2):
    alpha_1 = uniform(0, 1)
    alpha_2 = uniform(0, 1)
    o1 = [None] * len(p1)
    o2 = [None] * len(p1)
    for i in range(len(p1)):
        o1[i] = p1[i] * alpha_1 + (1-alpha_1) * p2[i]
        o2[i] = p2[i] * alpha_2 + (1-alpha_2) * p1[i]
    return o1, o2

def cycle_xo(p1, p2):
    """Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # offspring placeholders
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p1)

    while None in offspring1:
        index = offspring1.index(None)
        val1 = p1[index]
        val2 = p2[index]

        # copy the cycle elements
        while val1 != val2:
            offspring1[index] = p1[index]
            offspring2[index] = p2[index]
            val2 = p2[index]
            index = p1.index(val2)

        # copy the rest
        for element in offspring1:
            if element is None:
                index = offspring1.index(None)
                if offspring1[index] is None:
                    offspring1[index] = p2[index]
                    offspring2[index] = p1[index]

    print()
    return offspring1, offspring2

def pmx(p1, p2):
    """Implementation of partially matched/mapped crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    xo_points = sample(range(len(p1)), 2)
    #xo_points = [3,6]
    xo_points.sort()

    def pmx_offspring(x,y):
        o = [None] * len(x)
        # offspring2
        o[xo_points[0]:xo_points[1]]  = x[xo_points[0]:xo_points[1]]
        z = set(y[xo_points[0]:xo_points[1]]) - set(x[xo_points[0]:xo_points[1]])

        # numbers that exist in the segment
        for i in z:
            temp = i
            index = y.index(x[y.index(temp)])
            while o[index] is not None:
                temp = index
                index = y.index(x[temp])
            o[index] = i

        # numbers that doesn't exist in the segment
        while None in o:
            index = o.index(None)
            o[index] = y[index]
        return o

    o1, o2 = pmx_offspring(p1, p2), pmx_offspring(p2, p1)
    return o1, o2

def geometric_co(parent1, parent2):
    """Perform geometric crossover between two parents to produce offspring."""
    
    alpha_1=random()
    o1 = []
    for i in range(len(parent1)):
        gene1 = parent1[i]
        gene2 = parent2[i]
        new_gene = alpha_1 * gene1 + (1 - alpha_1) * gene2
        o1.append(new_gene)

    alpha_2=random()
    o2 = []
    for i in range(len(parent1)):
        gene1 = parent1[i]
        gene2 = parent2[i]
        new_gene = alpha_2 * gene1 + (1 - alpha_2) * gene2
        o2.append(new_gene)    

    return o1, o2
