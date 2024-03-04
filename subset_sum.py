import random
import sys

MUT_PROB = 0.5
POPULATION_SIZE = 10
GEN_SIZE = 1000


def find_indices(nums, target):
    population = [[random.randint(0, 1) for _ in range(len(nums))] for _ in range(POPULATION_SIZE)]

    def fitness_function(solution):
        # if all are 0 return massive number
        if not any(solution):
            return sys.maxsize
        return abs(sum(num for num, pick in zip(nums, solution) if
                       pick) - target)  # generator when pick 1 then num gets added to sum

    for i in range(GEN_SIZE):
        fitness_scores = [fitness_function(solution) for solution in population]
        best_solution = population[fitness_scores.index(min(fitness_scores))]
        if sum(num for num, pick in zip(nums, best_solution) if pick) == target:
            return best_solution

        new_population = []

        def crossover(p1, p2):
            c = [None] * len(nums)
            crossover_point = random.randrange(0, len(nums))
            c[crossover_point:] = p1[crossover_point:]
            c[:crossover_point] = p2[:crossover_point]
            return c

        def mutate(c):
            if random.random() < MUT_PROB:
                gene_to_mutate = random.randrange(0, len(nums))
                c[gene_to_mutate] = random.randint(0, 1)  # noqa

        for j in range(POPULATION_SIZE):
            parent1 = population[random.randrange(0, POPULATION_SIZE)]
            parent2 = population[random.randrange(0, POPULATION_SIZE)]
            child = crossover(parent1, parent2)
            mutate(child)

            new_population.append(child)

        population = new_population


def main():
    with open('input.txt', 'r') as file:
        n = file.readline().split()
        n1 = int(n[0])
        target = int(n[1])
        lst1 = []
        lst2 = []
        for _ in range(n1):
            s = file.readline().split()
            lst1.append(s[0])
            lst2.append(int(s[1]))
        
    indices = find_indices(lst2, target)
    if indices:
        out = "".join(map(str, indices))
    else:
        out = -1
    print(lst1)
    print(out)


main()