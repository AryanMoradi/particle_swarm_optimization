import random
import matplotlib.pyplot as plt
from optimization_problems import AckleyFunction
from pso_variants import Particle, PSO
from topologies import GlobalBestTopology, RingTopology, StarTopology, RandomNeighbourhoodConnectivity

def initialise_swarm(num_particles, num_dimensioms,position_range,velocity_range):
    particles = []
    for _ in range(num_particles):
        new_particle = Particle(num_dimensioms,position_range,velocity_range)
        particles.append(new_particle)

    return particles

#run on ackley function 10 times
for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = GlobalBestTopology(problem)
    pso = PSO(problem,50,1000,topology,10)
    x,global_fitness,swarm_centre_of_mass,standard_deviation,velocity_vector_length = pso.optimize()
    plt.scatter(x,global_fitness)
    plt.title("global_fitness")
    plt.show()
    plt.scatter(x,swarm_centre_of_mass)
    plt.title("swarm centre of mass distance")
    plt.show()
    plt.scatter(x,standard_deviation)
    plt.title("standard deviation")
    plt.show()
    plt.scatter(x,velocity_vector_length)
    plt.title("velocity")
    plt.show()
    


#repeat on swarm size 20,100,200
swarm_sizes = [20,100,200]

for size in swarm_sizes:
    problem = initialise_swarm(size,10,30,30)
    topology = GlobalBestTopology(problem)
    pso = PSO(problem,size,1000,topology,10)
    x,global_fitness,swarm_centre_of_mass,standard_deviation,velocity_vector_length = pso.optimize()
    plt.scatter(x,global_fitness)
    plt.title("global_fitness")
    plt.show()
    plt.scatter(x,swarm_centre_of_mass)
    plt.title("swarm centre of mass distance")
    plt.show()
    plt.scatter(x,standard_deviation)
    plt.title("standard deviation")
    plt.show()
    plt.scatter(x,velocity_vector_length)
    plt.title("velocity")
    plt.show()
    
    

#inertia weight adjustment


#neighbourhood topology comparison
#gbest

for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = GlobalBestTopology(problem)
    pso = PSO(problem,50,1000,topology,10)
    x,global_fitness,swarm_centre_of_mass,standard_deviation,velocity_vector_length = pso.optimize()
    plt.scatter(x,global_fitness)
    plt.title("global_fitness")
    plt.show()
    plt.scatter(x,swarm_centre_of_mass)
    plt.title("swarm centre of mass distance")
    plt.show()
    plt.scatter(x,standard_deviation)
    plt.title("standard deviation")
    plt.show()
    plt.scatter(x,velocity_vector_length)
    plt.title("velocity")
    plt.show()
    


#ring topology
for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = RingTopology(problem)
    pso = PSO(problem,50,1000,topology,10)
    x,global_fitness,swarm_centre_of_mass,standard_deviation,velocity_vector_length = pso.optimize()
    plt.scatter(x,global_fitness)
    plt.title("global_fitness")
    plt.show()
    plt.scatter(x,swarm_centre_of_mass)
    plt.title("swarm centre of mass distance")
    plt.show()
    plt.scatter(x,standard_deviation)
    plt.title("standard deviation")
    plt.show()
    plt.scatter(x,velocity_vector_length)
    plt.title("velocity")
    plt.show()
    

#neighbourhood_results.append(results)

#star
for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = StarTopology(problem)
    pso = PSO(problem,50,1000,topology,10)
    x,global_fitness,swarm_centre_of_mass,standard_deviation,velocity_vector_length = pso.optimize()
    plt.scatter(x,global_fitness)
    plt.title("global_fitness")
    plt.show()
    plt.scatter(x,swarm_centre_of_mass)
    plt.title("swarm centre of mass distance")
    plt.show()
    plt.scatter(x,standard_deviation)
    plt.title("standard deviation")
    plt.show()
    plt.scatter(x,velocity_vector_length)
    plt.title("velocity")
    plt.show()
    

#random
results = []
for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = RandomNeighbourhoodConnectivity(problem)
    pso = PSO(problem,50,1000,topology,10)
    x,global_fitness,swarm_centre_of_mass,standard_deviation,velocity_vector_length = pso.optimize()
    plt.scatter(x,global_fitness)
    plt.title("global_fitness")
    plt.show()
    plt.scatter(x,swarm_centre_of_mass)
    plt.title("swarm centre of mass distance")
    plt.show()
    plt.scatter(x,standard_deviation)
    plt.title("standard deviation")
    plt.show()
    plt.scatter(x,velocity_vector_length)
    plt.title("velocity")
    plt.show()
    






