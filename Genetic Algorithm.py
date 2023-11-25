import random
import math


class GeneticAlgorithm:
    def __init__(self, individual_size, population_size):
        self.population = []
        self.individual_size = individual_size
        self.population_size = population_size
        self.total_fitness = 0

        for _ in range(population_size):
            individual = [random.randint(0, 1) for _ in range(individual_size)]
            self.population.append([individual, sum(individual)])
            self.total_fitness += sum(individual)

    def update_population_fitness(self):
        self.total_fitness = sum(ind[1] for ind in self.population)

    def select_parents(self):
        roulette_wheel = []
        probabilities = [ind[1] / self.total_fitness for ind in self.population]

        for ind, prob in zip(self.population, probabilities):
            roulette_wheel.extend([ind] * round(prob * self.population_size * 5))

        random.shuffle(roulette_wheel)
        parents = [ind[0].copy() for ind in roulette_wheel[: self.population_size]]
        self.population = [[child, sum(child)] for child in parents]
        self.update_population_fitness()

    def generate_children(self, crossover_probability):
        num_pairs = round(crossover_probability * self.population_size / 2)

        for _ in range(num_pairs):
            parent1, parent2 = random.sample(self.population, 2)
            crossover_point = random.randint(0, self.individual_size - 1)
            child1 = parent1[0][:crossover_point] + parent2[0][crossover_point:]
            child2 = parent2[0][:crossover_point] + parent1[0][crossover_point:]
            self.population.extend([[child1, sum(child1)], [child2, sum(child2)]])

        self.update_population_fitness()

    def mutate_children(self, mutation_probability):
        num_bits = round(
            mutation_probability * self.population_size * self.individual_size
        )
        bit_indices = random.sample(
            range(self.population_size * self.individual_size), num_bits
        )

        for idx in bit_indices:
            ind_index = idx // self.individual_size
            bit_index = idx % self.individual_size
            self.population[ind_index][0][bit_index] = (
                1 - self.population[ind_index][0][bit_index]
            )

        self.update_population_fitness()


def binary_to_decimal(binary_list):
    binary_str = "".join(map(str, binary_list))
    decimal_value = int(binary_str, 2)
    return decimal_value


individual_size, population_size = 8, 10
generation = 0
ga_instance = GeneticAlgorithm(individual_size, population_size)

while True:
    ga_instance.select_parents()
    ga_instance.generate_children(0.8)
    ga_instance.mutate_children(0.03)

    best_individual = max(ga_instance.population, key=lambda k: k[1])

    print(f"Generation {generation}: Best Individual: {best_individual[0]}")
    generation += 1

    if best_individual[1] == individual_size:
        break
