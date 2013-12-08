Spanning Tree Problems
======================

Goal: Take a connected undirected graph, effectively remove edges until there are no cycles, while remaining connected.

Note: You'll always end up with at least n-1 edges (where n &equiv; number of nodes)

Algorithms
----------

Minimum cost (sum of edge costs is lowest possible):
* Kruskal's Method
* Prim's Method
* Sollin's Method &mdash; may fail, causing cycles
