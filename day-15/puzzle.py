import sys

from itertools import product
from queue import PriorityQueue


# Adapted from https://stackabuse.com/dijkstras-algorithm-in-python/
def dijkstra(graph, start_vertex):
    distances = {v: float('inf') for v in graph}
    distances[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, currentVertex) = pq.get()
        graph.visited.append(currentVertex)

        for neighbor in graph.neighbors(currentVertex):
            if graph.edges[currentVertex][neighbor] != -1:
                distance = graph.edges[currentVertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = distances[neighbor]
                    new_cost = distances[currentVertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        distances[neighbor] = new_cost
    return distances


class Graph:
    def __init__(self):
        self.grid = []
        self.rows = self.cols = 0
        for line in sys.stdin:
            data = list(map(int, line.rstrip()))
            if self.rows == 0:
                self.cols = len(data)
            else:
                assert self.cols == len(data)
            self.grid.append(data)
            self.rows += 1

    def addEdges(self):
        self.edges = {}
        self.visited = []

        for point in self:
            for neighbor in self.neighbors(point):
                self.addEdge(point, neighbor, self[neighbor])

    def __str__(self):
        result = ''
        for row in range(self.rows):
            for col in range(self.cols):
                result += str(self[(row, col)])
            result += '\n'
        return result

    def __iter__(self):
        return product(range(self.rows), range(self.cols))

    def __getitem__(self, point):
        return self.grid[point[0]][point[1]]

    def __setitem__(self, point, value):
        self.grid[point[0]][point[1]] = value

    def neighbors(self, point):
        r, c = point
        for row, col in ((r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)):
            if 0 <= row < self.rows and 0 <= col < self.cols:
                yield row, col

    def addEdge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = {}

        if v in self.edges[u]:
            assert self.edges[u][v] == weight, (
                f'{u} -> {v} is already {self.edges[u][v]}. New = {weight}')

        self.edges[u][v] = weight

    def extend(self, multiplier):
        def incRow(values, inc):
            for value in values:
                n = value + inc
                yield (n if n < 10 else n - 9)

        grid = []
        for row in self.grid:
            rowValues = []
            for increment in range(multiplier):
                rowValues.extend(list(incRow(row, increment)))
            grid.append(rowValues)

        top = grid.copy()

        for increment in range(1, multiplier):
            for row in top:
                grid.append(list(incRow(row, increment)))

        self.grid = grid
        self.rows *= multiplier
        self.cols *= multiplier
