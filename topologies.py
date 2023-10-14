import random
from optimization_problems import AckleyFunction

class GlobalBestTopology:
    def __init__(self, particles):
        self.type = "gbest"
        self.neighbour_list = []
        for _ in range(len(particles)):
            self.neighbour_list.append(particles)
                

class RingTopology:
    def __init__(self, particles):
        self.type = "ring"
        self.neighbour_list = []

        self.neighbour_list.append([particles[-1],particles[1]])
        for i in range(1,len(particles)-1):
            self.neighbour_list.append([particles[i-1],particles[i+1]])

        self.neighbour_list.append([particles[-2],particles[0]])

class StarTopology:
    def __init__(self,particles):
        self.update(particles)
        self.type = "star"

    def update(self,particles):
        fitness_function = AckleyFunction(dimensions=len(particles[0].position))
        best_fitness = fitness_function.evaluate(particles[0].position)
        current_best = particles[0]
        for particle in particles:
            fitness = fitness_function.evaluate(particle.position)
            if fitness < best_fitness:
                best_fitness = fitness
                current_best = particle

        self.neighbour_list = []

        for particle in particles:
            self.neighbour_list.append([particle, current_best])

class RandomNeighbourhoodConnectivity:
    def __init__(self,particles):
            self.type = "rand"
            self.update(particles)

    def update(self,particles):
        self.neighbour_list = []

        for particle in particles:
            neighbour_indices = random.sample(range(len(particles)), random.randint(1, len(particles) - 1))
            temp = [particle]
            for neighbour in neighbour_indices:
                temp.append(particles[neighbour])

            self.neighbour_list.append(temp)


