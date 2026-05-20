import time
import random
import matplotlib.pyplot as plt

from grid import create_grid
from pathfinding import AStarSearch


def show_step(grid, path, start, goal):

    plt.clf()
    plt.imshow(grid, cmap="gray_r", origin="upper")

    # draw path so far
    for p in path:
        plt.scatter(p[1], p[0], c="purple", s=20)

    # robot head
    if path:
        head = path[-1]
        plt.scatter(head[1], head[0], c="blue", s=120)

    # start & goal
    plt.scatter(start[1], start[0], c="green", s=120)
    plt.scatter(goal[1], goal[0], c="red", s=120)

    plt.pause(0.1)


def main():

    size = int(input("Grid size (e.g. 20): "))
    density = float(input("Obstacle density (0-1): "))

    grid = create_grid(size, density)

    start = (0, 0)

    # random goal (must be free cell)
    while True:
        goal = (
            random.randint(0, size - 1),
            random.randint(0, size - 1)
        )
        if grid[goal] == 0:
            break

    print("\nStart:", start)
    print("Goal:", goal)

    search = AStarSearch(grid, start, goal)
    path = search.run()

    if not path:
        print("\nNo path found.")
        return

    print("\nPath found!")
    print("Path length:", len(path) - 1)
    print("Nodes explored:", search.nodes_explored)

    plt.figure()

    for i in range(1, len(path) + 1):
        show_step(grid, path[:i], start, goal)
        time.sleep(0.1)

    plt.show()


if __name__ == "__main__":
    main()