#!/usr/bin/env python

from puzzle import main


class Path:
    def __init__(self):
        self.path = []
        self.smallSeen = set()

    def __hash__(self):
        return hash(tuple(self.path))

    def extend(self, vertex):
        assert self.okAsNext(vertex)
        if vertex.islower():
            self.smallSeen.add(vertex)
        self.path.append(vertex)

    def okAsNext(self, vertex):
        return vertex not in self.smallSeen

    def complete(self):
        return self.path[-1] == 'end'

    def last(self):
        return self.path[-1]

    def copy(self):
        new = Path()
        new.path = list(self.path)
        new.smallSeen = set(self.smallSeen)
        return new


if __name__ == '__main__':
    print(main(Path))
