import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import math


def random_points(n: int, x: int, y: int) -> list:
    return [(np.random.uniform(0, x),
             np.random.uniform(0, y))
            for _ in range(n)]


def plot_points(plotted_points: list):
    return [plt.scatter(x, y, color='red') for x, y in plotted_points]


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def each_point(pp: list, plot_number: int):
    plt.ion()

    # First 3 points
    p3 = [p for p in pp[0:3]]

    # Create pairs in a cyclic manner
    pairs = [(p3[i], p3[(i + 1) % len(p3)]) for i in range(len(p3))]

    count = 0

    for p in pp[3:]:

        # plot points
        plot_points(points)
        # Plot pair lines
        for pair in pairs:
            x_values = [pair[0][0], pair[1][0]]
            y_values = [pair[0][1], pair[1][1]]
            plt.plot(x_values, y_values, color='red', zorder=-1, alpha=.5, linestyle=':', linewidth=4)

        # Get distances (ab, ac + bc)
        distances_abc = [(distance(x, y), distance(p, x) + distance(p, y)) for x, y in pairs]

        # Calculate cost
        real_costs = [d2 - d1 for d1, d2 in distances_abc]

        # Get the lowest cost pair
        lowest_cost_index = min(range(len(real_costs)), key=real_costs.__getitem__)

        # Pair with new point
        new_pair = [(p, pairs[lowest_cost_index][0]), (p, pairs[lowest_cost_index][1])]

        # Plot pair lines
        for pair in new_pair:
            x_values = [pair[0][0], pair[1][0]]
            y_values = [pair[0][1], pair[1][1]]
            plt.plot(x_values, y_values, color='blue', zorder=1, linestyle=':', alpha=.5, linewidth=4)

        pairs = pairs + new_pair

        # Remove old pair
        del pairs[lowest_cost_index]

        # Plot pair lines
        for pair in pairs:
            x_values = [pair[0][0], pair[1][0]]
            y_values = [pair[0][1], pair[1][1]]
            plt.plot(x_values, y_values, color='green', zorder=1, alpha=.8)

        plt.show()  # Show plot

        # Save the plot to a file in the timestamped folder
        file_path = os.path.join(full_folder_path, f'{plot_number + 1}_plot_{count + 1}.png')
        count += 1

        plt.savefig(file_path)

        plt.pause(0.1)  # Pause for 1 second
        plt.clf()  # Clear the figure

    plot_points(points)

    # Plot pair lines
    for pair in pairs:
        x_values = [pair[0][0], pair[1][0]]
        y_values = [pair[0][1], pair[1][1]]
        plt.plot(x_values, y_values, color='gray', zorder=-1, linewidth=4)

    file_path = os.path.join(full_folder_path, f'{plot_number + 1}_plot_{count + 1}.png')
    plt.savefig(file_path)
    plt.show()  # Show plot
    plt.pause(1)  # Pause for 1 second
    plt.clf()  # Clear the figure


# Generate a timestamp
timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')  # Format timestamp as YYYY-MM-DD_HHMMSS

# Define the folder name
folder_name = f'plots_{timestamp}'

# Ensure the base directory exists
base_dir = 'plots'
os.makedirs(base_dir, exist_ok=True)

# Create the timestamped folder
full_folder_path = os.path.join(base_dir, folder_name)
os.makedirs(full_folder_path, exist_ok=True)

# Number of plots to generate
num_plots = 2

for c in range(num_plots):
    points = random_points(100, 100, 100)
    # plot_points(points)
    each_point(points, c)
