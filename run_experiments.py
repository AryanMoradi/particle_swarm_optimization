import random
import matplotlib.pyplot as plt
import metrics_and_visualization as mv
from pso_variants import Particle, PSO, GlobalBestTopology, inertia_weight_PSO, RingTopology, StarTopology, RandomNeighbourhoodConnectivity
import os

# Requirement 6


def run_experiment(swarm_size, num_runs=10, pso_type="standard",topology_type="gbest", file_name="metrics_std_pso.png"):
    num_particles = swarm_size
    num_dimensions = 10
    position_range = 30
    velocity_range = 30

    all_metrics_data = []

    for run in range(num_runs):
        problem = [Particle(num_dimensions, position_range, velocity_range)
                   for _ in range(num_particles)]
        
        if topology_type == "gbest":
            topology = GlobalBestTopology(problem)
        elif topology_type == "ring":
            topology = RingTopology(problem)
        elif topology_type == "star":
            topology = StarTopology(problem)
        else:
            topology = RandomNeighbourhoodConnectivity(problem)

        if pso_type == "standard":
            pso = PSO(problem, num_particles, 1000, topology, num_dimensions)
        else:
            pso = inertia_weight_PSO(problem, num_particles, 1000, topology, num_dimensions)

        x, global_fitness, swarm_centre_of_mass, standard_deviation, velocity_vector_length = pso.optimize()

        metrics_data = {
            "iterations": x,
            "best_fitness": global_fitness,
            "distance_to_optimum": swarm_centre_of_mass,
            "std_dev_positions": standard_deviation,
            "mean_velocity": velocity_vector_length
        }

        all_metrics_data.append(metrics_data)

    mv.plot_metrics(all_metrics_data)

    plt.savefig("results/" + file_name)


#part6 
run_experiment(30,file_name="metrics_std_pso.png")

#part7
run_experiment(20,file_name="metrics_std_pso_swarm20.png")
run_experiment(100,file_name="metrics_std_pso_swarm100.png")
run_experiment(200,file_name="metrics_std_pso_swarm200.png")

#part8 
run_experiment(30,pso_type="inertia",file_name="metrics_std_pso_weight adjust.png")

#part9 
run_experiment(30, file_name="metrics_std_pso_topo_gbest.png")
run_experiment(30,topology_type="ring", file_name="metrics_std_pso_topo_ring.png")
run_experiment(30,topology_type="star", file_name="metrics_std_pso_topo_star.png")
run_experiment(30,topology_type="rand", file_name="metrics_std_pso_topo_rand.png")
