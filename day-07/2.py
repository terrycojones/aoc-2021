#!/usr/bin/env python

import sys


def moveCost(n):
    return int(n * (n + 1) / 2)


positions = list(map(int, sys.stdin.read().rstrip().split(',')))

maxMoveCost = moveCost(max(positions) - min(positions))
minCost = len(positions) * maxMoveCost

for p in range(max(positions) + 1):
    cost = sum(moveCost(abs(position - p)) for position in positions)
    if cost < minCost:
        minCost = cost

print(minCost)
