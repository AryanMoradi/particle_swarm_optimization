import random
from optimization_problems import AckleyFunction


class GlobalBestTopology:
    def __init__(self, particles):
        self.type = "gbest"
        self.neighbour_list = []
        for _ in range(len(particles)):
            self.neighbour_list.append(range(len(particles)))


class RingTopology:
    def __init__(self, particles):
        self.type = "ring"
        self.neighbour_list = []

        self.neighbour_list.append([len(particles)-1, 1])
        for i in range(1, len(particles)-1):
            self.neighbour_list.append([i-1, i+1])

        self.neighbour_list.append([len(particles)-2, 0])


class StarTopology:
    def __init__(self, particles):
        self.update(particles)
        self.type = "star"

    def update(self, particles):
        fitness_function = AckleyFunction(
            dimensions=len(particles[0].position))
        best_fitness = fitness_function.evaluate(particles[0].position)
        current_best_index = 0
        for i in range(1, len(particles)):
            fitness = fitness_function.evaluate(particles[i].position)
            if fitness < best_fitness:
                best_fitness = fitness
                current_best_index = i

        self.neighbour_list = []

        for i in range(len(particles)):
            self.neighbour_list.append([i, current_best_index])


class RandomNeighbourhoodConnectivity:
    def __init__(self, particles):
        self.type = "rand"
        self.update(particles)

    def update(self, particles):
        self.neighbour_list = []

        for particle in particles:
            neighbour_indices = random.sample(
                range(len(particles)), random.randint(0, len(particles) - 1))
            self.neighbour_list.append(neighbour_indices)
