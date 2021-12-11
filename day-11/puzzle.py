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

    def __setitem__(self, point, value):
        self.grid[point[0]][point[1]] = value

    def neighbors(self, point):
        r, c = point
        for row, col in ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                         (r, c - 1), (r, c + 1),
                         (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)):
            if 0 <= row < self.rows and 0 <= col < self.cols:
                yield row, col

    def increment(self):
        for point in self:
            self[point] += 1

    def reset(self):
        for point in self:
            if self[point] > 9:
                self[point] = 0

    def flash(self):
        flashed = set()
        for point in self:
            if self[point] > 9:
                flashed.add(point)

        incremented = set(flashed)

        while incremented:
            todo = set(incremented)
            incremented = set()
            for point in todo:
                for neighbor in self.neighbors(point):
                    if neighbor not in incremented and neighbor not in flashed:
                        self[neighbor] += 1
                        if self[neighbor] > 9:
                            flashed.add(neighbor)
                            incremented.add(neighbor)

        return len(flashed)

    def run(self, steps=1):
        flashes = 0
        for _ in range(steps):
            self.increment()
            flashes += self.flash()
            self.reset()
        return flashes
