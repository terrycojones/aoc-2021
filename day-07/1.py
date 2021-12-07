#!/usr/bin/env python

import sys

positions = list(map(int, sys.stdin.read().rstrip().split(',')))

maxMoveCost = max(positions) - min(positions)
minCost = len(positions) * maxMoveCost

for p in range(max(positions) + 1):
    cost = sum(abs(position - p) for position in positions)
    if cost < minCost:
        minCost = cost

print(minCost)
