import sys

import numpy as np


def calc(state, days, cache):
    if days == 0:
        return 1

    result = cache[state, days]

    if result == 0:
        if state == 0:
            newState = 6
            offspring = calc(8, days - 1, cache)
        else:
            newState = state - 1
            offspring = 0

        result = calc(newState, days - 1, cache) + offspring
        cache[state, days] = result

    return result


def main(days):
    states = list(map(int, sys.stdin.read().rstrip().split(',')))
    cache = np.zeros((9, days + 1), dtype=int)
    return sum(calc(state, days, cache) for state in states)


def mainSlow(days):
    # Original solution to part 1.
    states = list(map(int, sys.stdin.read().rstrip().split(',')))

    for day in range(days):
        eights = 0
        for i, fish in enumerate(states):
            if fish == 0:
                eights += 1
                states[i] = 6
            else:
                states[i] -= 1

        states.extend([8] * eights)

    return len(states)
