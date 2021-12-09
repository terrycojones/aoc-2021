import sys


class Grid:
    def __init__(self):
        self.grid = []
        first = True
        n = None
        for line in sys.stdin:
            data = list(map(int, line.rstrip()))
            if first:
                n = len(data)
                first = False
            else:
                assert n == len(data)
            self.grid.append(data)

    def __iter__(self):
        return ((row, col)
                for row in range(len(self.grid))
                for col in range(len(self.grid[0])))

    def __getitem__(self, point):
        return self.grid[point[0]][point[1]]

    def neighbors(self, point):
        row, col = point
        maxRow = len(self.grid)
        maxCol = len(self.grid[0])
        for r, c in ((row, col - 1), (row, col + 1),
                     (row - 1, col), (row + 1, col)):
            if 0 <= r < maxRow and 0 <= c < maxCol:
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
            for neighbor in self.uphillNeighbors(point):
                if neighbor not in seen:
                    neighbours.add(neighbor)

        return sum(self[point] < 9 for point in seen)

    def basinSizes(self):
        return [self.basinSize(point) for point in self.lowPoints()]

    def totalRisk(self):
        return sum(self[point] + 1 for point in self.lowPoints())
