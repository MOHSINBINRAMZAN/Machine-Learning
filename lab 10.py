<<<<<<< HEAD
import random

# Define the parameters
population_size = 10
chromosome_length = 8
mutation_rate = 0.1
generations = 100

# Initialize population
def initialize_population(population_size, chromosome_length):
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(population_size)]

# Evaluate fitness of individuals
def fitness(individual):
    # Placeholder fitness function, replace this with your implementation
    # Return a numerical value indicating the fitness of the individual
    return sum(individual)

# Select parents for crossover
def selection(population):
    # Select individuals based on their fitness
    # You can use various selection methods like roulette wheel, tournament, etc.
    return random.choice(population), random.choice(population)

# Perform crossover
def crossover(parent1, parent2):
    # Randomly select a crossover point
    crossover_point = random.randint(1, len(parent1) - 1)
    
    # Create offspring by combining genes of parents
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return child1, child2

# Perform mutation
def mutation(individual, mutation_rate):
    # Randomly mutate genes with a given mutation rate
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip the bit

# Genetic Algorithm
def genetic_algorithm(population_size, chromosome_length, mutation_rate, generations):
    population = initialize_population(population_size, chromosome_length)

    for generation in range(generations):
        # Evaluate fitness of the population
        fitness_scores = [fitness(individual) for individual in population]
        
        # Select parents
        parent1, parent2 = selection(population)
        
        # Perform crossover and mutation to create new population
        new_population = []
        for _ in range(population_size // 2):
            child1, child2 = crossover(parent1, parent2)
            mutation(child1, mutation_rate)
            mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        
        # Replace the old population with the new population
        population = new_population

    # Return the best individual in the final population
    best_individual = max(population, key=fitness)
    return best_individual

# Example usage
best_solution = genetic_algorithm(population_size, chromosome_length, mutation_rate, generations)
print("Best solution:", best_solution)
print("Fitness:", fitness(best_solution))
=======
import random

# Define the parameters
population_size = 10
chromosome_length = 8
mutation_rate = 0.1
generations = 100

# Initialize population
def initialize_population(population_size, chromosome_length):
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(population_size)]

# Evaluate fitness of individuals
def fitness(individual):
    # Placeholder fitness function, replace this with your implementation
    # Return a numerical value indicating the fitness of the individual
    return sum(individual)

# Select parents for crossover
def selection(population):
    # Select individuals based on their fitness
    # You can use various selection methods like roulette wheel, tournament, etc.
    return random.choice(population), random.choice(population)

# Perform crossover
def crossover(parent1, parent2):
    # Randomly select a crossover point
    crossover_point = random.randint(1, len(parent1) - 1)
    
    # Create offspring by combining genes of parents
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return child1, child2

# Perform mutation
def mutation(individual, mutation_rate):
    # Randomly mutate genes with a given mutation rate
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip the bit

# Genetic Algorithm
def genetic_algorithm(population_size, chromosome_length, mutation_rate, generations):
    population = initialize_population(population_size, chromosome_length)

    for generation in range(generations):
        # Evaluate fitness of the population
        fitness_scores = [fitness(individual) for individual in population]
        
        # Select parents
        parent1, parent2 = selection(population)
        
        # Perform crossover and mutation to create new population
        new_population = []
        for _ in range(population_size // 2):
            child1, child2 = crossover(parent1, parent2)
            mutation(child1, mutation_rate)
            mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        
        # Replace the old population with the new population
        population = new_population

    # Return the best individual in the final population
    best_individual = max(population, key=fitness)
    return best_individual

# Example usage
best_solution = genetic_algorithm(population_size, chromosome_length, mutation_rate, generations)
print("Best solution:", best_solution)
print("Fitness:", fitness(best_solution))
>>>>>>> e0d3d757fa858b53a002a1dad5388be5b4af4699
