#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    for x in line.split(' | ')[1].strip().split():
        count += len(x) in {2, 3, 4, 7}

print(count)
