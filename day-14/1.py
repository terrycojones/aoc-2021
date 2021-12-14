#!/usr/bin/env python

from puzzle import readInput
from collections import Counter


if __name__ == '__main__':
    template, moves = readInput()

    for _ in range(10):
        result = ''
        for index in range(len(template) - 1):
            result += template[index] + moves[template[index:index+2]]
        template = result + template[-1]

    m = Counter(template).most_common()
    print(m[0][1] - m[-1][1])
