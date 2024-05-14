<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

# Objective function
def objective_function(x):
    return x**2

# Hill climbing optimization algorithm
def hill_climbing_optimization(obj_func, initial_x, step_size, max_iterations):
    current_x = initial_x

    for _ in range(max_iterations):
        # Evaluate the current point
        current_value = obj_func(current_x)

        # Evaluate the next point
        next_x = current_x + step_size
        next_value = obj_func(next_x)

        # Update the current point if the next point has a lower function value
        if next_value < current_value:
            current_x = next_x

    return current_x, obj_func(current_x)

# Set up the optimization parameters
initial_x = -4.0  # Initial guess
step_size = 0.1   # Step size for hill climbing
max_iterations = 50  # Maximum number of iterations

# Run hill climbing optimization
optimal_x, optimal_value = hill_climbing_optimization(objective_function, initial_x, step_size, max_iterations)

# Generate a grid of input values for plotting
x_values = np.linspace(-5, 5, 100)
y_values = objective_function(x_values)

# Create a line plot of the response surface
plt.plot(x_values, y_values, label='Objective Function')

# Mark the optimum point found by hill climbing
plt.scatter(optimal_x, optimal_value, color='green', marker='o', label=f'Optimal Point\nx={optimal_x:.2f}, f(x)={optimal_value:.2f}')

# Mark the known optimum point at f(0.0) = 0.0 with a red line
plt.axvline(x=0.0, color='red', linestyle='--', label='Known Optimum at x=0.0')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Hill Climbing Optimization of Objective Function')

# Add legend
plt.legend()

# Show the plot
plt.show()

=======
import numpy as np
import matplotlib.pyplot as plt

# Objective function
def objective_function(x):
    return x**2

# Hill climbing optimization algorithm
def hill_climbing_optimization(obj_func, initial_x, step_size, max_iterations):
    current_x = initial_x

    for _ in range(max_iterations):
        # Evaluate the current point
        current_value = obj_func(current_x)

        # Evaluate the next point
        next_x = current_x + step_size
        next_value = obj_func(next_x)

        # Update the current point if the next point has a lower function value
        if next_value < current_value:
            current_x = next_x

    return current_x, obj_func(current_x)

# Set up the optimization parameters
initial_x = -4.0  # Initial guess
step_size = 0.1   # Step size for hill climbing
max_iterations = 50  # Maximum number of iterations

# Run hill climbing optimization
optimal_x, optimal_value = hill_climbing_optimization(objective_function, initial_x, step_size, max_iterations)

# Generate a grid of input values for plotting
x_values = np.linspace(-5, 5, 100)
y_values = objective_function(x_values)

# Create a line plot of the response surface
plt.plot(x_values, y_values, label='Objective Function')

# Mark the optimum point found by hill climbing
plt.scatter(optimal_x, optimal_value, color='green', marker='o', label=f'Optimal Point\nx={optimal_x:.2f}, f(x)={optimal_value:.2f}')

# Mark the known optimum point at f(0.0) = 0.0 with a red line
plt.axvline(x=0.0, color='red', linestyle='--', label='Known Optimum at x=0.0')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Hill Climbing Optimization of Objective Function')

# Add legend
plt.legend()

# Show the plot
plt.show()

>>>>>>> e0d3d757fa858b53a002a1dad5388be5b4af4699
