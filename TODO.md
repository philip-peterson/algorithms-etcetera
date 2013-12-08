Spanning Tree Problems
======================

Goal: Take a connected undirected graph, effectively remove edges until there are no cycles, while remaining connected.

Note: You'll always end up with at least n-1 edges (where n &equiv; number of nodes)

Algorithms
----------

Minimum cost (sum of edge costs is lowest possible) algorithms:
* Kruskal's Method
    - O(n + e log e) using union-find trees
* Prim's Method
    - O(n^2) using implementation similar to Dijkstra's algorithm
    - O(e + n log n) using Fibonacci heap
* Sollin's Method &mdash; may fail, causing cycles
