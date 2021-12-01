#!/usr/bin/env python

import sys

data = [int(line) for line in sys.stdin]

print(sum(sum(data[index - 2:index + 1]) > sum(data[index - 3:index])
          for index in range(3, len(data))))
