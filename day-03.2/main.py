#!/usr/bin/env python

import sys

from collections import Counter
from itertools import count


def filter_(lines, offset, mostCommonOffset, tieBreak):
    common = Counter(line[offset] for line in lines).most_common()

    if len(common) == 1:
        wanted = common[0][0]
    else:
        if common[0][1] == common[1][1]:
            wanted = tieBreak
        else:
            wanted = common[mostCommonOffset][0]

    return [line for line in lines if line[offset] == wanted]


def getRating(lines, mostCommonOffset, tieBreak):
    for offset in count():
        lines = filter_(lines, offset, mostCommonOffset, tieBreak)
        if len(lines) == 1:
            return int(lines[0], 2)


def main():
    lines = [line.rstrip() for line in sys.stdin]
    oxygen = getRating(lines, 0, '1')
    co2 = getRating(lines, 1, '0')
    print(oxygen * co2)


if __name__ == '__main__':
    main()
