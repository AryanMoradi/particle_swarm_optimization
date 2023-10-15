import random
import matplotlib.pyplot as plt
from optimization_problems import AckleyFunction
from pso_variants import Particle, PSO, GlobalBestTopology
import metrics_and_visualization as mv


def run_experiment(swarm_size):
    num_particles = swarm_size
    num_dimensions = 10
    position_range = 30
    velocity_range = 30

    problem = [Particle(num_dimensions, position_range, velocity_range)
               for _ in range(num_particles)]
    topology = GlobalBestTopology(problem)
    pso = PSO(problem, num_particles, 1000, topology, num_dimensions)

    # Optimize on Ackley function
    x, global_fitness, swarm_centre_of_mass, standard_deviation, velocity_vector_length = pso.optimize()

    # Create a metrics dictionary to store data
    metrics_data = {
        "iterations": x,
        "best_fitness": global_fitness,
        "distance_to_optimum": swarm_centre_of_mass,
        "std_dev_positions": standard_deviation,
        "mean_velocity": velocity_vector_length
    }

    # Plot the metrics
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    # Plot best fitness value vs iterations
    ax[0, 0].plot(metrics_data["iterations"],
                  metrics_data["best_fitness"], label="Best Fitness")
    ax[0, 0].set_title("Best Fitness vs Iterations")
    ax[0, 0].set_xlabel("Iterations")
    ax[0, 0].set_ylabel("Best Fitness")
    ax[0, 0].legend()

    # Plot distance to global optimum vs iterations
    ax[0, 1].plot(metrics_data["iterations"],
                  metrics_data["distance_to_optimum"], label="Distance to Optimum")
    ax[0, 1].set_title("Distance to Global Optimum vs Iterations")
    ax[0, 1].set_xlabel("Iterations")
    ax[0, 1].set_ylabel("Distance to Optimum")
    ax[0, 1].legend()

    # Plot standard deviation of particle positions vs iterations
    ax[1, 0].plot(metrics_data["iterations"],
                  metrics_data["std_dev_positions"], label="Std Dev of Positions")
    ax[1, 0].set_title(
        "Standard Deviation of Particle Positions vs Iterations")
    ax[1, 0].set_xlabel("Iterations")
    ax[1, 0].set_ylabel("Std Dev of Positions")
    ax[1, 0].legend()

    # Plot mean velocity vs iterations
    ax[1, 1].plot(metrics_data["iterations"],
                  metrics_data["mean_velocity"], label="Mean Velocity")
    ax[1, 1].set_title("Mean Velocity vs Iterations")
    ax[1, 1].set_xlabel("Iterations")
    ax[1, 1].set_ylabel("Mean Velocity")
    ax[1, 1].legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # You can specify different swarm sizes here
    swarm_sizes = [20, 100, 200]

    for swarm_size in swarm_sizes:
        run_experiment(swarm_size)
