import sys
from copy import deepcopy
from collections import defaultdict


def main(pathClass):
    edges = defaultdict(set)
    for line in sys.stdin:
        start, end = line.rstrip().split('-')
        edges[start].add(end)
        edges[end].add(start)

    assert 'start' in edges
    p = pathClass()
    p.extend('start')

    incomplete = {p}
    complete = set()

    while incomplete:
        path = incomplete.pop()

        for vertex in edges[path.last()]:
            if path.okAsNext(vertex):
                new = deepcopy(path)
                new.extend(vertex)
                if new.complete():
                    if new not in complete:
                        complete.add(new)
                else:
                    if new not in incomplete:
                        incomplete.add(new)

    return len(complete)
