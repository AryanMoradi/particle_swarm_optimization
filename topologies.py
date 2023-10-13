import random

class GlobalBestTopology:
    def __init__(self, particles):
        self.type = "gbest"
        self.neighour_list = []
        for _ in range(len(particles)):
            self.neighbour_list.append(particles)
                

class RingTopology:
    def __init__(self, particles):
        self.type = "ring"
        self.neighour_list = []

        self.neighour_list.append([particles[-1],particles[1]])
        for i in range(1,len(particles)-1):
            self.neighbour_list.append([particles[i-1],particles[i+1]])

        self.neighour_list.append([particles[-2],particles[0]])

class StarTopology:
    def __init__(self,particles):
        self.update(particles)
        self.type = "star"

    def update(self,particles):
        best_fitness = get_fitness(particles[0])
        current_best = particles[0]
        for particle in particles:
            fitness = get_fitness(particle)
            if fitness > best_fitness:
                best_fitness = fitness
                current_best = particle

        self.neighour_list = []

        for particle in particles:
            self.neighour_list.append([particle, current_best])

class RandomNeighbourhoodConnectivity:
    def __init__(self,particles):
            self.type = "rand"
            self.update(particles)

    def update(self,particles):
        self.neighour_list = []

        for particle in particles:
            neighbor_indices = random.sample(range(len(particles)), random.randint(1, len(particles) - 1))
            temp = [particle]
            for neighbour in neighbor_indices:
                temp.append(particles[neighbour])

            self.neighour_list.append(temp)


