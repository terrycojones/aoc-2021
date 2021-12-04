import sys

from board import readBoards


def readInput():
    calls = list(map(int, next(sys.stdin).split(',')))
    boards = readBoards(sys.stdin)

    return calls, boards
