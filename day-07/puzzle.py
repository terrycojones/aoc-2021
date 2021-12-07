import sys


def main():
    positions = list(map(int, sys.stdin.read().rstrip().split(',')))

    minCost = sum(positions)
    for p in range(max(positions)):
        cost = sum(abs(position - p) for position in positions)
        if cost < minCost:
            minCost = cost

    return minCost
