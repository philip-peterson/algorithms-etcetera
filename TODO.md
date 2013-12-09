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


Max / Min Problems
==================

Algorithms
----------
* Divide and Conquer Max+Min &mdash; O(&lceil;3n/2&rceil; - 2)
    - Recursive version
    - Iterative version
* Multi-pass iterative Max/Min
    - I'm not sure this is better than D&C, but the D&C algorithm seems like it stops short of efficiency
* Iterative Linear Max/Min &mdash; O(n-1)
* Iterative Linear Max+Min &mdash; O(2n-2)
* Heap Max/Min
    - n > 1 &mdash; t(n) = 2t(n/2) + d * height
    - n <= 1 &mdash; t(n) = c
    - c and d are constants
    - Overall: O(n)
* Loser Tree Max/Min
    - n > 1 &mdash; t(n) = 2t(n/2) + d
    - n <= 1 &mdash; t(n) = c
    - c and d are constants
    - Overall: O(n)


Sort
====


Selection Problems
==================

Goal: select the nth smallest element from an unordered list.

* Selection by sorting - O(n log n)
* Divide and conquer selection (like Quicksort)
    - O(n^2) with a poorly chosen pivot
    - O(n) with clever pivot choosing

Closest Pair Problems
=====================

* Brute force - O(n^2)
* Divide and conquer - O(n log n)
