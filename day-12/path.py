class _Path:
    def __init__(self):
        self.path = []
        self.smallsSeen = set()

    def __hash__(self):
        return hash(tuple(self.path))

    def last(self):
        return self.path[-1]

    def complete(self):
        return self.last() == 'end'

    def extend(self, vertex):
        self.path.append(vertex)
        if vertex.islower():
            self.smallsSeen.add(vertex)


class NoDuplicatePath(_Path):
    def okAsNext(self, vertex):
        return vertex not in self.smallsSeen


class OneSmallDuplicatePath(_Path):
    def __init__(self):
        super().__init__()
        self.duplicatedSmall = None

    def okAsNext(self, vertex):
        if vertex == self.duplicatedSmall or vertex == 'start':
            return False

        if vertex in self.smallsSeen:
            return self.duplicatedSmall is None

        return True

    def extend(self, vertex):
        if vertex in self.smallsSeen:
            assert self.duplicatedSmall is None
            self.duplicatedSmall = vertex
        super().extend(vertex)
