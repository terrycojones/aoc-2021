#!/usr/bin/env python

import sys
from puzzle import readInput


def main():
    calls, boards = readInput()
    nBoards = len(boards)
    finished = 0

    for call in calls:
        for index, board in enumerate(boards):
            if board:
                board.call(call)
                if board.bingo():
                    finished += 1
                    if finished == nBoards:
                        print(call * board.total())
                        sys.exit()
                    boards[index] = None


if __name__ == '__main__':
    main()
