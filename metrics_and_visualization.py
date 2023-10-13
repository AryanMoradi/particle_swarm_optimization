import matplotlib.pyplot as plt
import numpy as np

def gather_metrics(swarm):

    best_fitness = swarm.gbest_value
    distance_to_optimum = np.linalg.norm(swarm.gbest_position)
    std_dev_positions = np.std(swarm.positions)
    mean_velocity = np.mean(np.linalg.norm(swarm.velocities, axis=1))

    return {
        "best_fitness": best_fitness,
        "distance_to_optimum": distance_to_optimum,
        "std_dev_positions": std_dev_positions,
        "mean_velocity": mean_velocity
    }

def plot_metrics(metrics_data):

    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    # Plot best fitness value vs iterations
    ax[0, 0].plot(metrics_data["iterations"], metrics_data["best_fitness"], label="Best Fitness")
    ax[0, 0].set_title("Best Fitness vs Iterations")
    ax[0, 0].set_xlabel("Iterations")
    ax[0, 0].set_ylabel("Best Fitness")
    ax[0, 0].legend()

    # Plot distance to global optimum vs iterations
    ax[0, 1].plot(metrics_data["iterations"], metrics_data["distance_to_optimum"], label="Distance to Optimum")
    ax[0, 1].set_title("Distance to Global Optimum vs Iterations")
    ax[0, 1].set_xlabel("Iterations")
    ax[0, 1].set_ylabel("Distance to Optimum")
    ax[0, 1].legend()

    # Plot standard deviation of particle positions vs iterations
    ax[1, 0].plot(metrics_data["iterations"], metrics_data["std_dev_positions"], label="Std Dev of Positions")
    ax[1, 0].set_title("Standard Deviation of Particle Positions vs Iterations")
    ax[1, 0].set_xlabel("Iterations")
    ax[1, 0].set_ylabel("Std Dev of Positions")
    ax[1, 0].legend()

    # Plot mean velocity vs iterations
    ax[1, 1].plot(metrics_data["iterations"], metrics_data["mean_velocity"], label="Mean Velocity")
    ax[1, 1].set_title("Mean Velocity vs Iterations")
    ax[1, 1].set_xlabel("Iterations")
    ax[1, 1].set_ylabel("Mean Velocity")
    ax[1, 1].legend()

    plt.tight_layout()
    plt.show()