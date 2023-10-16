import numpy as np
import random
from statistics import stdev
from optimization_problems import AckleyFunction
from topologies import GlobalBestTopology, RingTopology, StarTopology, RandomNeighbourhoodConnectivity


class Particle:
    def __init__(self, num_dimensions, position_range, velocity_range):
        self.velocity = [
            random.uniform(-velocity_range, velocity_range) for _ in range(num_dimensions)]
        self.position = [
            random.uniform(-position_range, position_range) for _ in range(num_dimensions)]
        fitness_function = AckleyFunction(dimensions=num_dimensions)
        self.best_fitness = fitness_function.evaluate(
            self.position)  # Initialize with fitness value
        self.best_position = self.position
        self.best_neighbour_position = self.position
        self.best_neighbour_fitness = self.best_fitness


#standard pso
class PSO:
    def __init__(self, problem, num_particles, max_iterations, topology, num_dimensions):
        self.problem = problem
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.topology = topology
        self.num_dimensions = num_dimensions
        self.global_best_position = None
        self.global_best_fitness = float('inf')

    def initialize_particles(self):
        fitness_function = AckleyFunction(dimensions=self.num_dimensions)
        for particle in self.problem:
            particle.best_position = particle.position
            particle.best_fitness = fitness_function.evaluate(
                particle.position)
            if particle.best_fitness < self.global_best_fitness:
                self.global_best_fitness = particle.best_fitness
                self.global_best_position = particle.position

    def optimize(self):
        fitness_function = AckleyFunction(dimensions=self.num_dimensions)
        x = []
        global_fitness = []
        swarm_centre_of_mass = []
        standard_deviation = []
        velocity_vector_length = []

        self.initialize_particles()

        for i in range(self.max_iterations):
            all_positions = []
            all_vectors = []

            if self.topology.type == "rand":
                self.topology.update(self.problem)

            for particle in range(self.num_particles):
                all_positions.append(self.problem[particle].position)
                all_vectors.append(self.problem[particle].velocity)

                fitness = fitness_function.evaluate(
                    self.problem[particle].position)

                if fitness < self.problem[particle].best_fitness:
                    self.problem[particle].best_position = self.problem[particle].position
                    self.problem[particle].best_fitness = fitness

                if fitness < self.global_best_fitness:
                    self.global_best_fitness = fitness
                    self.global_best_position = self.problem[particle].position

                if self.topology.type == "gbest":
                    self.problem[particle].best_neighbour_position = self.global_best_position
                    self.problem[particle].best_neighbour_fitness = self.global_best_fitness
                else:
                    for neighbour in self.topology.neighbour_list[particle]:
                        fitness = fitness_function.evaluate(self.problem[neighbour].position)
                        if fitness < self.problem[particle].best_neighbour_fitness:
                            self.problem[particle].best_neighbour_position = self.problem[neighbour].position
                            self.problem[particle].best_neighbour_fitness = fitness

                self.update(particle)

            if self.topology.type == "star":
                self.topology.update(self.problem)

            x.append(i + 1)
            global_fitness.append(self.global_best_fitness)

            mean = np.average(all_positions, axis=0)
            swarm_centre_of_mass.append(
                np.linalg.norm(self.global_best_position - mean))

            distances = np.linalg.norm(all_positions - mean, axis=1)
            standard_deviation.append(stdev(distances))

            mean_velocity = np.average(all_vectors, axis=0)
            sum_velocity = np.sum(np.abs(mean_velocity))
            velocity_vector_length.append(sum_velocity / self.num_dimensions)

            if self.global_best_fitness < 1e-6:
                break

        return x, global_fitness, swarm_centre_of_mass, standard_deviation, velocity_vector_length

    def update(self, particle_index):
        particle = self.problem[particle_index]
        # Vid = Vid + Ce1(Pid-Xid) + Ce2(Pgd-Xid)
        e1 = [random.uniform(0, 1) for i in range(self.num_dimensions)]
        e2 = [random.uniform(0, 1) for i in range(self.num_dimensions)]
        for d in range(self.num_dimensions):
            particle.velocity[d] = particle.velocity[d] + 2*e1[d]*(particle.best_position[d]-particle.position[d]) + 2*e2[d]*(
                particle.best_neighbour_position[d]-particle.position[d])
            particle.position[d] = particle.position[d] + particle.velocity[d]
        self.problem[particle_index] = particle
        return

#inertia weight pso
class inertia_weight_PSO(PSO):
    #overrride update function
    def update(self, particle_index):
        particle = self.problem[particle_index]
        e1 = [random.uniform(0, 1) for _ in range(self.num_dimensions)]
        e2 = [random.uniform(0, 1) for _ in range(self.num_dimensions)]
        inertia_weight = 0.5  # Inertia weight
        cognitive_weight = 1.5  # Cognitive component weight
        social_weight = 1.5  # Social component weight

        for d in range(self.num_dimensions):
            inertia_term = inertia_weight * particle.velocity[d]
            cognitive_component = cognitive_weight * e1[d] * \
                (particle.best_position[d] - particle.position[d])
            social_component = social_weight * e2[d] * \
                (self.global_best_position[d] - particle.position[d])
            particle.velocity[d] = inertia_term + \
                cognitive_component + social_component
            particle.position[d] = particle.position[d] + particle.velocity[d]
        self.problem[particle_index] = particle