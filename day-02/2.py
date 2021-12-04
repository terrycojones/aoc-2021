#!/usr/bin/env python

import sys

horizontal = depth = aim = 0

for line in sys.stdin:
    action, x = line.split()
    x = int(x)
    if action == 'down':
        aim += x
    elif action == 'up':
        aim -= x
    elif action == 'forward':
        horizontal += x
        depth += aim * x
    else:
        raise ValueError(action)

print(horizontal * depth)
