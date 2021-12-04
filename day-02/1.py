#!/usr/bin/env python

import sys
from collections import Counter

data = Counter()

for line in sys.stdin:
    action, x = line.split()
    data[action] += int(x)

print(data['forward'] * (data['down'] - data['up']))
