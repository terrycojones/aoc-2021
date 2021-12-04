#!/usr/bin/env python

import sys
from puzzle import readInput


def main():
    calls, boards = readInput()

    for call in calls:
        for board in boards:
            board.call(call)
            if board.bingo():
                print(call * board.total())
                sys.exit()


if __name__ == '__main__':
    main()
