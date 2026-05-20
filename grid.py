import numpy as np
import random


def create_grid(size=20, obstacle_density=0.35):

    grid = np.zeros((size, size), dtype=int)

    # vertical warehouse shelves
    for i in range(0, size, 4):
        for j in range(size):
            if random.random() < obstacle_density:
                grid[j][i] = 1

    # horizontal shelves
    for i in range(0, size, 5):
        for j in range(size):
            if random.random() < obstacle_density:
                grid[i][j] = 1

    # extra random obstacles
    for _ in range(int(size * size * 0.1)):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        grid[x][y] = 1

    return grid