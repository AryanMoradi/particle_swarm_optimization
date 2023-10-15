import random
import matplotlib.pyplot as plt
import metrics_and_visualization as mv
from pso_variants import Particle, PSO, GlobalBestTopology
import os

# Requirement 6


def run_experiment(swarm_size, num_runs=10):
    num_particles = swarm_size
    num_dimensions = 10
    position_range = 30
    velocity_range = 30

    all_metrics_data = []

    for run in range(num_runs):
        problem = [Particle(num_dimensions, position_range, velocity_range)
                   for _ in range(num_particles)]
        topology = GlobalBestTopology(problem)

        pso = PSO(problem, num_particles, 1000, topology, num_dimensions)

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

    plt.savefig("results/metrics_std_pso.png")


run_experiment(30)
