#!/usr/bin/env python

import sys


def fingerprint(reference, patterns):
    result = []
    for pattern in patterns:
        if pattern != reference:
            result.append((len(reference | pattern), len(reference - pattern),
                           len(pattern - reference)))
    result.sort()
    return tuple(result)


patterns = list(map(set, ('abcefg cf acdeg acdfg bcdf abdfg '
                          'abdefg acf abcdefg abcdfg').split()))

canonical = dict((fingerprint(pattern, patterns), digit)
                 for digit, pattern in zip('0123456789', patterns))

total = 0

for line in sys.stdin:
    left, right = line.split(' | ')
    observations = list(map(frozenset, left.split()))
    digits = dict((obs, canonical[fingerprint(obs, observations)])
                  for obs in observations)
    outputs = list(map(frozenset, right.strip().split()))
    total += int(''.join(digits[output] for output in outputs))

print(total)
