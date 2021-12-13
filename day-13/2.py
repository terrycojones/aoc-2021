#!/usr/bin/env python

from puzzle import readInput


if __name__ == '__main__':
    grid, folds = readInput()
    for axis, n in folds:
        grid = grid.fold(axis, n)

    print(grid)
    print()
    print(grid.hflip())
