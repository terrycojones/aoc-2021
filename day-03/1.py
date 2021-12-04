#!/usr/bin/env python

import sys

from collections import Counter

first = True

for line in sys.stdin:
    bits = list(line.rstrip())
    if first:
        counters = [Counter() for _ in bits]
        first = False

    for i, bit in enumerate(bits):
        counters[i][bit] += 1

gamma = epsilon = ''

for counter in counters:
    # Make sure there were no draws.
    assert counter['0'] != counter['1']
    common = counter.most_common()
    gamma += common[0][0]
    epsilon += common[1][0]

print(int(gamma, 2) * int(epsilon, 2))
