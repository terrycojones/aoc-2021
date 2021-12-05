import sys
import numpy as np


def readInput():
    result = []
    x = []
    y = []
    for line in sys.stdin:
        start, end = line.rstrip().split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        x.extend((x1, x2))
        y.extend((y1, y2))
        result.append(((x1, y1), (x2, y2)))

    return result, max(x), max(y)


def main(includeDiagonals=False):
    coords, maxX, maxY = readInput()
    grid = np.zeros((maxY + 1, maxX + 1), dtype=int)

    for ((x1, y1), (x2, y2)) in coords:
        if x1 == x2:
            minY, maxY = sorted((y1, y2))
            for y in range(minY, maxY + 1):
                grid[y][x1] += 1
        elif y1 == y2:
            minX, maxX = sorted((x1, x2))
            for x in range(minX, maxX + 1):
                grid[y1][x] += 1
        else:
            if includeDiagonals:
                # Check coords are ok (x diff == y diff).
                assert abs(x1 - x2) == abs(y1 - y2)

                xInc = 1 if x1 < x2 else -1
                yInc = 1 if y1 < y2 else -1
                x, y = x1 - xInc, y1 - yInc

                while x != x2:
                    x += xInc
                    y += yInc
                    grid[y][x] += 1

    return np.sum(grid > 1)
