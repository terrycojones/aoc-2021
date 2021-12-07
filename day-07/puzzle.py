import sys


def main(cost):
    positions = list(map(int, sys.stdin.read().split(',')))

    return min(sum(cost(abs(position - answer)) for position in positions)
               for answer in range(min(positions), max(positions) + 1))
