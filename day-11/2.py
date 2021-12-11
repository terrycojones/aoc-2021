#!/usr/bin/env python

from puzzle import Grid


if __name__ == '__main__':
    grid = Grid()
    total = grid.rows * grid.cols
    step = 0
    while True:
        step += 1
        flashes = grid.run()
        if flashes == total:
            print(step)
            break
