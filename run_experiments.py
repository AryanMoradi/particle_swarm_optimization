import random
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
results = []
for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = GlobalBestTopology(problem)
    pso = PSO(problem,50,1000,30,30,topology)
    pso.opitimize()
    results.append(pso.problem)

#send results to graphing function

#repeat on swarm size 20,100,200
swarm_sizes = [20,100,200]

results = []
for size in swarm_sizes:
    problem = initialise_swarm(size,10,30,30)
    topology = GlobalBestTopology(problem)
    pso = PSO(problem,size,1000,30,30,topology)
    pso.opitimize()
    results.append(pso.problem)

#send results to graphing function


#inertia weight adjustment


#neighbourhood topology comparison
neighbourhood_results = []
#gbest
results = []
for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = GlobalBestTopology(problem)
    pso = PSO(problem,50,1000,30,30,topology)
    pso.opitimize()
    results.append(pso.problem)
neighbourhood_results.append(results)
#ring topology
results = []
for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = RingTopology(problem)
    pso = PSO(problem,50,1000,30,30,topology)
    pso.opitimize()
    results.append(pso.problem)
neighbourhood_results.append(results)
#star
results = []
for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = StarTopology(problem)
    pso = PSO(problem,50,1000,30,30,topology)
    pso.opitimize()
    results.append(pso.problem)
neighbourhood_results.append(results)
#random
results = []
for _ in range(10):
    problem = initialise_swarm(50,10,30,30)
    topology = RandomNeighbourhoodConnectivity(problem)
    pso = PSO(problem,50,1000,30,30,topology)
    pso.opitimize()
    results.append(pso.problem)
neighbourhood_results.append(results)

#send neighbourhood results to graphing function




