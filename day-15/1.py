#!/usr/bin/env python

from puzzle import dijkstra, Graph


if __name__ == '__main__':
    graph = Graph()
    graph.addEdges()
    d = dijkstra(graph, (0, 0))
    print(d[(graph.rows - 1, graph.cols - 1)])
