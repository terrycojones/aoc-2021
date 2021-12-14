import sys


def readInput():
    template = next(sys.stdin).rstrip()
    next(sys.stdin)
    points = {}
    for line in sys.stdin:
        from_, to = line.rstrip().split(' -> ')
        assert from_ not in points
        points[from_] = to

    return template, points
