import sys
from itertools import product


class Grid:
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

    def __iter__(self):
        return product(range(self.rows), range(self.cols))

    def __getitem__(self, point):
        return self.grid[point[0]][point[1]]

    def neighbors(self, point):
        row, col = point
        for r, c in ((row, col - 1), (row, col + 1),
                     (row - 1, col), (row + 1, col)):
            if 0 <= r < self.rows and 0 <= c < self.cols:
                yield r, c

    def uphillNeighbors(self, point):
        value = self[point]
        return (n for n in self.neighbors(point) if self[n] > value)

    def lowPoint(self, point):
        value = self[point]
        return all(value < self[point] for point in self.neighbors(point))

    def lowPoints(self):
        return (point for point in self if self.lowPoint(point))

    def basinSize(self, point):
        seen = set()
        neighbours = {point}
        while neighbours:
            point = neighbours.pop()
            seen.add(point)
            neighbours.update(n for n in self.uphillNeighbors(point)
                              if n not in seen)
        return sum(self[point] < 9 for point in seen)

    def basinSizes(self):
        return [self.basinSize(point) for point in self.lowPoints()]

    def totalRisk(self):
        return sum(self[point] + 1 for point in self.lowPoints())
