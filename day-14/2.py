#!/usr/bin/env python

from puzzle import readInput
from collections import defaultdict


if __name__ == '__main__':
    template, moves = readInput()

    counts = defaultdict(int)
    for index in range(len(template) - 1):
        counts[template[index:index+2]] += 1

    for _ in range(40):
        nextCounts = defaultdict(int)
        for key, count in counts.items():
            move = moves[key]
            nextCounts[key[0] + move] += count
            nextCounts[move + key[1]] += count
        counts = nextCounts

    letters = defaultdict(int)
    for key, count in counts.items():
        letters[key[0]] += count
    letters[template[-1]] += 1

    s = sorted(letters, key=lambda x: letters[x])

    print(letters[s[-1]] - letters[s[0]])
