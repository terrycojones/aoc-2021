import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def countFish(args):
    state, days = args

    if days == 0:
        return 1

    if state == 0:
        newState = 6
        offspring = countFish((8, days - 1))
    else:
        newState = state - 1
        offspring = 0

    return countFish((newState, days - 1)) + offspring


def main(days):
    states = list(map(int, sys.stdin.read().rstrip().split(',')))
    return sum(countFish((state, days)) for state in states)
