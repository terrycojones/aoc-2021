#!/usr/bin/env python

from puzzle import Grid


if __name__ == '__main__':
    sizes = sorted(Grid().basinSizes())
    print(sizes[-3] * sizes[-2] * sizes[-1])
