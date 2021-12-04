#!/usr/bin/env python

from puzzle import readInput


def main():
    calls, boards = readInput()

    for call in calls:
        for board in boards:
            board.call(call)
            if board.bingo():
                return call * board.total()


if __name__ == '__main__':
    print(main())
