import sys
import numpy as np

PAIR = {'(': ')', '[': ']', '{': '}', '<': '>'}
CLOSING = set(PAIR.values())
OK, CORRUPT, EMPTY_STACK, BAD_SYMBOL, INCOMPLETE = range(5)


def check(line):
    stack = []
    for i, symbol in enumerate(line):
        if symbol in PAIR:
            stack.append(symbol)
        else:
            if symbol in CLOSING:
                if stack:
                    if symbol == PAIR[stack[-1]]:
                        stack.pop()
                    else:
                        return CORRUPT, i, stack
                else:
                    return EMPTY_STACK, i, stack
            else:
                return BAD_SYMBOL, i, stack

    if stack:
        return INCOMPLETE, i, stack
    else:
        return 1, i, stack


def main1():
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in sys.stdin:
        line = line.strip()
        ok, offset, stack = check(line)
        if ok == CORRUPT:
            score += points[line[offset]]
        elif ok == EMPTY_STACK:
            print('empty stack', ok, offset, line)
        elif ok == BAD_SYMBOL:
            print('bad symbol ', ok, offset, line)
        elif ok == INCOMPLETE:
            pass
        else:
            print('line ok')

    return score


def main2():
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in sys.stdin:
        line = line.strip()
        ok, offset, stack = check(line)
        if ok == CORRUPT:
            pass
        elif ok == EMPTY_STACK:
            print('empty stack', ok, offset, line)
        elif ok == BAD_SYMBOL:
            print('bad symbol ', ok, offset, line)
        elif ok == INCOMPLETE:
            score = 0
            for symbol in reversed(stack):
                score = 5 * score + points[PAIR[symbol]]
            scores.append(score)
        else:
            print('line ok')

    assert len(scores) % 2
    return int(np.median(sorted(scores)))
