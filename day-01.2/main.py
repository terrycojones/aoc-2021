#!/usr/bin/env python

import sys

data = [int(line) for line in sys.stdin]

increases = 0

for index in range(3, len(data)):
    this = sum(data[index - 2:index + 1])
    prev = sum(data[index - 3:index])
    if this > prev:
        increases += 1

print(increases)
