import sys
from copy import copy
from collections import defaultdict


def main(pathClass):
    edges = defaultdict(set)
    vertices = set()
    for line in sys.stdin:
        start, end = line.rstrip().split('-')
        edges[start].add(end)
        edges[end].add(start)
        vertices.update((start, end))

    assert 'start' in vertices
    p = pathClass()
    p.extend('start')

    incomplete = {p}
    complete = set()

    while incomplete:
        path = incomplete.pop()

        for vertex in edges[path.last()]:
            if path.okAsNext(vertex):
                new = copy(path)
                new.extend(vertex)
                if new.complete():
                    if new not in complete:
                        complete.add(new)
                else:
                    if new not in incomplete:
                        incomplete.add(new)

    return len(complete)
