import numpy as np
import random

# assumes that particle class has the following variables: position, velocity, best individual position, best position of any neighbours
# assumes fitness has been implemented elsewhere and can be imported


class Particle:
    def __init__(self, num_dimensions):
        self.velocity = []
        self.position = []
        self.num_dimensions = num_dimensions
        self.velocity = random.uniform(-100, 100, num_dimensions)
        self.position = random.uniform(-100, 100, num_dimensions)
        self.best_position = self.position
        self.best_neighbour_position = self.position


class PSO:
    def __init__(self, problem, num_particles, max_iterations, topology):
        # initialise components
        self.problem = problem
        self.num_particles = num_particles
        self.max_iterations = max_iterations

    def optimize(self):
        # for each time step t
        for _ in range(self.max_iterations):
            # initialize random topology
            if topology.type == "rand":
                topology.update(self.problem)
            for particle in range(self.num_particles):
                # update position and velocity
                self.update(particle)

                # calculate particle fitness and update best individual fitness
                fitness = get_fitness(self.problem[particle])

                # update individual fitness if better
                if fitness > self.problem[particle].best_position:
                    self.problem[particle].best_position = fitness

                # update neighbour fitness if better
                for neighbour in topology.neighbour_list[particle]:
                    fitness = get_fitness(self.problem[neighbour])
                    if fitness > self.problem[particle].best_neighbour_position:
                        self.problem[particle].best_neighbour_position = fitness

            # update if star topology
            if topology.type == "star":
                topology.update(self.problem)

    def update(self, particle_index):
        particle = self.problem[particle_index]
        # Vid = Vid + Ce1(Pid-Xid) + Ce2(Pgd-Xid)
        e1 = random.uniform(0, 1, particle.num_dimensions)
        e2 = random.uniform(0, 1, particle.num_dimensions)
        for d in particle.num_dimensions:
            particle.velocity[d] = particle.velocity[d] + 2*e1[d]*(particle.best_position[d]-particle.position[d]) + 2*e2[d]*(
                particle.best_neighbour_position[d]-particle.position[d])
            particle.position[d] = particle.position[d] + particle.velocity[d]
        self.problem[particle_index] = particle
        return
