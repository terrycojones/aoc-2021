import sys


def readInput():
    points = []
    for line in sys.stdin:
        line = line.rstrip()
        if line:
            col, row = map(int, line.split(','))
            points.append((row, col))
        else:
            break

    folds = []
    for line in sys.stdin:
        assert line.startswith('fold along ')
        axis, n = line.split()[2].split('=')
        folds.append((axis, int(n)))

    return Grid(points), folds


class Grid:
    def __init__(self, points):
        self.points = points
        self.rows = max(row for row, _ in points)
        self.cols = max(col for _, col in points)

    def __str__(self):
        grid = []
        for _ in range(self.rows + 1):
            grid.append([' '] * (self.cols + 1))

        for row, col in self.points:
            grid[row][col] = '#'

        return '\n'.join(''.join(row) for row in grid)

    def hflip(self):
        points = set()
        for row, col in self.points:
            points.add((row, self.cols - col))

        return Grid(points)

    def foldLeft(self, n):
        points = set()
        for row, col in self.points:
            points.add((row, col - n - 1) if col > n else (row, n - col - 1))

        # Sanity check no over-folding.
        assert all([row >= 0 and col >= 0 and col < n for row, col in points])
        return Grid(points)

    def foldUp(self, n):
        points = set()
        for row, col in self.points:
            points.add((n - (row - n), col) if row > n else (row, col))

        # Sanity check no over-folding.
        assert all([row >= 0 and col >= 0 and row < n for row, col in points])
        return Grid(points)

    def fold(self, axis, n):
        return self.foldLeft(n) if axis == 'x' else self.foldUp(n)
