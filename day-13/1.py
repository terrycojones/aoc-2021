#!/usr/bin/env python

from puzzle import readInput


if __name__ == '__main__':
    grid, folds = readInput()
    axis, n = folds[0]
    print(len(grid.fold(axis, n).points))
