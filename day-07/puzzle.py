import sys


def main(moveCost):
    positions = list(map(int, sys.stdin.read().rstrip().split(',')))

    return min(sum(moveCost(abs(position - p)) for position in positions)
               for p in range(min(positions), max(positions) + 1))
