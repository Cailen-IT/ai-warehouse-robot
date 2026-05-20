import heapq


class AStarSearch:

    def __init__(self, grid, start, goal):

        self.grid = grid
        self.start = start
        self.goal = goal

        self.rows, self.cols = grid.shape

        self.open_nodes = []
        self.closed_nodes = set()
        self.parent = {}

        self.g_cost = {start: 0}
        self.f_cost = {start: self.heuristic(start)}

        heapq.heappush(self.open_nodes, (self.f_cost[start], start))

        self.nodes_explored = 0

    def heuristic(self, node):

        dx = abs(node[0] - self.goal[0])
        dy = abs(node[1] - self.goal[1])

        return (dx + dy) * 0.9

    def get_neighbors(self, node):

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        neighbors = []

        for dx, dy in directions:

            x = node[0] + dx
            y = node[1] + dy

            if 0 <= x < self.rows and 0 <= y < self.cols:

                if self.grid[x][y] == 0:
                    neighbors.append((x, y))

        return neighbors

    def reconstruct_path(self, current):

        path = [current]

        while current in self.parent:
            current = self.parent[current]
            path.append(current)

        return path[::-1]

    def run(self):

        while self.open_nodes:

            _, current = heapq.heappop(self.open_nodes)
            self.nodes_explored += 1

            if current == self.goal:
                return self.reconstruct_path(current)

            self.closed_nodes.add(current)

            for neighbor in self.get_neighbors(current):

                if neighbor in self.closed_nodes:
                    continue

                new_g = self.g_cost[current] + 1

                if neighbor not in self.g_cost or new_g < self.g_cost[neighbor]:

                    self.parent[neighbor] = current
                    self.g_cost[neighbor] = new_g

                    f_val = new_g + self.heuristic(neighbor)
                    self.f_cost[neighbor] = f_val

                    heapq.heappush(self.open_nodes, (f_val, neighbor))

        return None