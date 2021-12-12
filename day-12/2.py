#!/usr/bin/env python

from puzzle import main
from path import OneSmallDuplicatePath


class Path:
    def __init__(self):
        self.path = []
        self.smallSeen = set()
        self.duplicate = None

    def __hash__(self):
        return hash(tuple(self.path))

    def __lt__(self, other):
        return tuple(self.path) < tuple(other.path)

    def __str__(self):
        return ' -> '.join(self.path) + f'\t(DUP: {self.duplicate})'

    def extend(self, vertex):
        if self.path:
            assert self.okAsNext(vertex)
        if vertex.islower():
            if vertex in self.smallSeen:
                assert self.duplicate is None
                self.duplicate = vertex
            else:
                self.smallSeen.add(vertex)
        self.path.append(vertex)

    def okAsNext(self, vertex):
        if vertex == self.duplicate or vertex == 'start':
            return False

        if vertex in self.smallSeen:
            return not self.duplicate

        return True

    def complete(self):
        return self.path[-1] == 'end'

    def last(self):
        return self.path[-1]

    def copy(self):
        new = Path()
        new.path = list(self.path)
        new.smallSeen = set(self.smallSeen)
        new.duplicate = self.duplicate
        return new


if __name__ == '__main__':
    print(main(OneSmallDuplicatePath))
