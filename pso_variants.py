import numpy as np
import random
from statistics import stdev
from topologies import GlobalBestTopology, RingTopology, StarTopology, RandomNeighbourhoodConnectivity
from optimization_problems import AckleyFunction


class Particle:
    def __init__(self, num_dimensions, lower_bound, upper_bound):
        self.position = np.random.uniform(
            lower_bound, upper_bound, num_dimensions)
        self.velocity = np.random.uniform(-0.1, 0.1, num_dimensions)
        self.personal_best_position = np.copy(self.position)
        self.personal_best_fitness = float('inf')

    def update_velocity(self, global_best_position, inertia_weight=0.5, cognitive_weight=1.5, social_weight=1.5):

        e1 = np.random.rand(len(self.position))
        e2 = np.random.rand(len(self.position))

        cognitive_component = cognitive_weight * e1 * \
            (self.personal_best_position - self.position)
        social_component = social_weight * e2 * \
            (global_best_position - self.position)

        self.velocity = inertia_weight * self.velocity + \
            cognitive_component + social_component

    def update_position(self, lower_bound, upper_bound):
        self.position = self.position + self.velocity
        self.position = np.clip(self.position, lower_bound, upper_bound)


# standard pso
class PSO:
    def __init__(self, problem, num_particles=30, max_iterations=1000, topology='gbest', num_neighbors=2):
        self.problem = problem
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.topology = topology
        self.global_best_position = np.random.uniform(
            problem.lower_bound, problem.upper_bound, problem.get_dimensions())
        self.global_best_fitness = float('inf')
        print(problem.get_dimensions())
        self.swarm = [Particle(problem.get_dimensions(
        ), problem.lower_bound, problem.upper_bound) for _ in range(num_particles)]
        self.num_neighbors = num_neighbors
        if self.topology == 'random':
            self.random_neighbourhood_connectivity = [np.random.choice(
                self.num_particles, self.num_neighbors, replace=False) for _ in range(self.num_particles)]
        self.global_fitness = []
        self.swarm_centre_of_mass = []
        self.standard_deviation = []
        self.velocity_vector_length = []

    def optimize(self):
        for i in range(self.max_iterations):
            best_fitness_this_iteration = float('inf')

            all_positions = []
            all_vectors = []

            for particle in self.swarm:
                fitness = self.problem.evaluate(particle.position)
                all_positions.append(particle.position)
                all_vectors.append(particle.velocity)

                if fitness < particle.personal_best_fitness:
                    particle.personal_best_fitness = fitness
                    particle.personal_best_position = particle.position.copy()

                if fitness < self.global_best_fitness:
                    self.global_best_fitness = fitness
                    self.global_best_position = particle.position.copy()

                best_fitness_this_iteration = min(
                    best_fitness_this_iteration, fitness)

            self.global_fitness.append(best_fitness_this_iteration)
            center_of_mass = np.mean(all_positions, axis=0)
            self.swarm_centre_of_mass.append(np.linalg.norm(center_of_mass))
            self.standard_deviation.append(np.std(all_positions))
            self.velocity_vector_length.append(
                np.mean([np.linalg.norm(v) for v in all_vectors]))

            for index, particle in enumerate(self.swarm):
                if self.topology == 'gbest':
                    best_position = GlobalBestTopology.get_best_position(
                        self, index)
                elif self.topology == 'ring':
                    best_position = RingTopology.get_best_position(
                        self, index)
                elif self.topology == 'star':
                    best_position = StarTopology.get_best_position(
                        self, index)
                elif self.topology == 'random':
                    best_position = RandomNeighbourhoodConnectivity.get_best_position(
                        self, index)
                else:
                    raise ValueError(
                        f"Topology {self.topology} is not supported")
                particle.update_velocity(best_position)
                particle.update_position(
                    self.problem.lower_bound, self.problem.upper_bound)
            if len(self.global_fitness) > 50 and best_fitness_this_iteration == self.global_fitness[i-49]:
                break
        return range(1, len(self.global_fitness)+1)
