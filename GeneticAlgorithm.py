import random

# Define parameters
POP_SIZE = 500
GENE_SIZE = 50
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.005
CROSSOVER_RATE = 0.9

# Define fitness function
def fitness(individual):
    cnt=0
    for i in individual:
      if i==1:
        cnt=cnt+1
    return cnt

# Generate initial population
population = []
for i in range(POP_SIZE):
    individual = [random.randint(0, 1) for j in range(GENE_SIZE)]
    population.append(individual)

# Main loop
for generation in range(MAX_GENERATIONS):
    # Evaluate fitness of each individual
    fitness_scores = [fitness(individual) for individual in population]

    # Select parents for crossover
    parents = random.choices(population, weights=fitness_scores, k=2)

    # Perform crossover and mutation to generate new offspring
    offspring = []
    for i in range(POP_SIZE):
        child = []
        for j in range(GENE_SIZE):
            if random.random() < CROSSOVER_RATE:
                child.append(parents[0][j])
            else:
                child.append(parents[1][j])
            if random.random() < MUTATION_RATE:
                child[j] = 1 - child[j]
        offspring.append(child)

    # Replace least fit individuals with new offspring
    population = sorted(population, key=fitness, reverse=True)
    population[POP_SIZE//2:] = offspring[:POP_SIZE//2]

    # Print best individual of current generation
    best_individual = max(population, key=fitness)
    print(f"Generation {generation}: {best_individual} (fitness={fitness(best_individual)})")
