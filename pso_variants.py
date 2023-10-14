import numpy as np
import random
from statistics import stdev
from optimization_problems import AckleyFunction
from topologies import GlobalBestTopology, RingTopology, StarTopology, RandomNeighbourhoodConnectivity

# assumes that particle class has the following variables: position, velocity, best individual position, best position of any neighbours
# assumes fitness has been implemented elsewhere and can be imported


class Particle:
    def __init__(self,num_dimensions,position_range,velocity_range):
        self.velocity = []
        self.position = []
        self.velocity = [random.uniform(-velocity_range,velocity_range) for i in range(num_dimensions)]
        self.position = [random.uniform(-position_range,position_range) for i in range(num_dimensions)]
        self.best_position = self.position
        fitness_function = AckleyFunction(dimensions=num_dimensions)
        self.best_fitness = fitness_function.evaluate(self.position)
        self.best_neighbour_position = self.position
        self.best_neighbour_fitness = self.best_fitness


class PSO:
    def __init__(self, problem, num_particles, max_iterations, topology,num_dimensions):
        # initialise components
        self.problem = problem
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.topology = topology
        self.num_dimensions = num_dimensions

    def optimize(self):
        fitness_function = AckleyFunction(dimensions=self.num_dimensions)
        global_best_fitness = fitness_function.evaluate(self.problem[0].position)
        global_best_position = self.problem[0].position
        x = []
        global_fitness = []
        swarm_centre_of_mass = []
        standard_deviation = []
        velocity_vector_length = []
        for i in range(self.max_iterations):
            #arrays for graphing data
            all_positions = []
            all_vectors = []
            #initialize random topology
            if self.topology.type == "rand":
                self.topology.update(self.problem)
            for particle in range(self.num_particles):
                all_positions.append(self.problem[particle].position)
                all_vectors.append(self.problem[particle].velocity)
                # update position and velocity
                self.update(particle)

                #calculate particle fitness and update best individual fitness
                fitness = fitness_function.evaluate(self.problem[particle].position)

                # update individual fitness if better
                if fitness < self.problem[particle].best_fitness:
                    self.problem[particle].best_position = self.problem[particle].position
                    self.problem[particle].best_fitness = fitness

                #update global fitness if better
                if fitness < global_best_fitness:
                    global_best_fitness = fitness
                    global_best_position = self.problem[particle].position

                # update neighbour fitness if better
                for neighbour in self.topology.neighbour_list[particle]:
                    fitness = fitness_function.evaluate(neighbour.position)
                    if fitness < self.problem[particle].best_neighbour_fitness:
                        self.problem[particle].best_neighbour_position = neighbour.position
                        self.problem[particle].best_neighbour_fitness = fitness

            
            #append graph metrics
            x.append(i+1)
            global_fitness.append(global_best_fitness)

            #append swarm distance
            mean = np.average(all_positions, axis=0)
            swarm_centre_of_mass.append(np.linalg.norm(global_best_position-mean))

            #append standard deviation
            distances = np.linalg.norm(all_positions - mean, axis=1)
            standard_deviation.append(stdev(distances))

            #append mean velocity length
            mean_velocity = np.average(all_vectors, axis=0)
            sum = float(0)
            for velocity in mean_velocity:
                sum += abs(velocity)
            velocity_vector_length.append(sum/self.num_dimensions)

            #update if star topology
            if self.topology.type == "star":
                self.topology.update(self.problem)

            #check convergence
            if global_best_fitness < 1e-6:
                break
        return (x,global_fitness,swarm_centre_of_mass,standard_deviation,velocity_vector_length)

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
