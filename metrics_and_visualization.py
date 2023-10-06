import matplotlib.pyplot as plt
import distinctpy

def plot_metrics(metrics_data):
    iterations = metrics_data['iterations']
    fitness_values = metrics_data['fitness_values']
    
    # Create a new figure
    plt.figure(figsize=(10, 5))
    
    # Create the first sub-figure 
    plt.subplot(1, 1, 1)
    plt.plot(iterations, fitness_values, marker='o', linestyle='-')
    plt.title('Current Best Fitness Value Over Iterations')
    plt.xlabel('Iterations')
    plt.ylabel('Fitness Value')
    
    # Create and display the graph
    plt.tight_layout()  
    plt.show()

def gather_metrics(swarm):
    pass

def run_optimization(swarm_class, problem, num_particles, max_iterations, topology, runs=10):
    pass