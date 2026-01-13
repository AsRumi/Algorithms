# Floyd-Warshall Algorithm

## Purpose

Floyd-Warshall algorithm is used to find the **shortest distance between all pairs of vertices** in a given weighted graph (directed or undirected).

## Why Not Just Use Dijkstra's?

Although Dijkstra's algorithm solves the shortest path problem, it only does so for **one source vertex at a time**.

- To find shortest paths from **all vertices** to all other vertices using Dijkstra's, you would need to run it n times (once for each vertex)
- Time complexity: O(n³) using a simple implementation, or O(n² log n) with a priority queue
- Floyd-Warshall achieves O(n³) but is simpler to implement and works with **negative edge weights** (as long as there are no negative cycles)

## Approach: Dynamic Programming with Adjacency Matrix

Floyd-Warshall uses **dynamic programming** to incrementally build up the solution by considering each vertex to be an intermediate between other pairs of vertices.

### Step 1: Create Initial Adjacency Matrix

Start by creating an adjacency matrix where:

- `matrix[i][j]` = weight of direct edge from vertex i to vertex j (if it exists)
- `matrix[i][j]` = ∞ if no direct path exists from i to j
- `matrix[i][i]` = 0 (distance from a vertex to itself is always 0)

### Step 2: Iterative Refinement

Refine this matrix **n times** (where n = number of vertices). In each iteration k:

- Consider vertex k as a potential **intermediate vertex**
- For every pair of vertices (i, j), check:
  - Is the direct path `dist[i][j]` shorter, OR
  - Is the path through vertex k (`dist[i][k] + dist[k][j]`) shorter?
- Update: `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

### Key Insight

After iteration k, the matrix contains the shortest paths between all pairs of vertices using **only vertices 0 through k as intermediate vertices**.

After all n iterations, you have the shortest paths between all pairs considering **all possible intermediate vertices**.

## Example Walkthrough

Consider this directed graph with 4 vertices:

```
Edges:
1 → 2 (weight 3)
1 → 4 (weight 7)
2 → 1 (weight 8)
2 → 3 (weight 2)
3 → 4 (weight 1)
3 → 1 (weight 5)
4 → 1 (weight 2)
```

### Initial Matrix (Direct Paths Only)

```
     1    2    3    4
1 [  0    3    ∞    7  ]
2 [  8    0    2    ∞  ]
3 [  5    ∞    0    1  ]
4 [  2    ∞    ∞    0  ]
```

### After Iteration 0 (Using Vertex 1 as Intermediate)

Check if paths improve by going through vertex 1:

- `dist[2][4]` = min(∞, dist[2][1] + dist[1][4]) = min(∞, 8 + 7) = 15
- `dist[3][2]` = min(∞, dist[3][1] + dist[1][2]) = min(∞, 5 + 3) = 8
- `dist[3][4]` = min(1, dist[3][1] + dist[1][4]) = min(1, 5 + 7) = 1
- `dist[4][2]` = min(∞, dist[4][1] + dist[1][2]) = min(∞, 2 + 3) = 5
- `dist[4][3]` = min(∞, dist[4][1] + dist[1][3]) = min(∞, 2 + ∞) = ∞
- And so on...

```
     1    2    3    4
1 [  0    3    ∞    7  ]
2 [  8    0    2   15  ]
3 [  5    8    0    1  ]
4 [  2    5    ∞    0  ]
```

### After Iteration 1 (Using Vertex 2 as Intermediate)

Now check if paths improve by going through vertex 2:

- `dist[1][3]` = min(∞, dist[1][2] + dist[2][3]) = min(∞, 3 + 2) = 5
- `dist[3][1]` = min(5, dist[3][2] + dist[2][1]) = min(5, 8 + 8) = 5
- `dist[4][1]` = min(2, dist[4][2] + dist[2][1]) = min(2, 5 + 8) = 2
- `dist[4][3]` = min(∞, dist[4][2] + dist[2][3]) = min(∞, 5 + 2) = 7

```
     1    2    3    4
1 [  0    3    5    7  ]
2 [  8    0    2    15 ]
3 [  5    8    0    1  ]
4 [  2    5    7    0  ]
```

### After Iteration 2 (Using Vertex 3 as Intermediate)

Check paths through vertex 3:

- `dist[1][4]` = min(7, dist[1][3] + dist[3][4]) = min(7, 5 + 1) = 6
- `dist[1][1]` = min(0, dist[1][3] + dist[3][1]) = min(0, 5 + 5) = 0
- `dist[2][4]` = min(15, dist[2][3] + dist[3][4]) = min(15, 2 + 1) = 3
- `dist[2][1]` = min(8, dist[2][3] + dist[3][1]) = min(8, 2 + 5) = 7
- `dist[4][1]` = min(2, dist[4][3] + dist[3][1]) = min(2, 7 + 5) = 2

```
     1    2    3    4
1 [  0    3    5    6  ]
2 [  7    0    2    3  ]
3 [  5    8    0    1  ]
4 [  2    5    7    0  ]
```

### After Iteration 3 (Using Vertex 4 as Intermediate)

Final refinement through vertex 4:

- `dist[1][1]` = min(0, dist[1][4] + dist[4][1]) = min(0, 6 + 2) = 0
- `dist[2][1]` = min(7, dist[2][4] + dist[4][1]) = min(7, 3 + 2) = 5
- `dist[2][2]` = min(0, dist[2][4] + dist[4][2]) = min(0, 3 + 5) = 0
- `dist[3][2]` = min(8, dist[3][4] + dist[4][2]) = min(8, 1 + 5) = 6
- No other improvements

### Final Matrix (All-Pairs Shortest Paths)

```
     1    2    3    4
1 [  0    3    5    6  ]
2 [  5    0    2    3  ]
3 [  5    6    0    1  ]
4 [  2    5    7    0  ]
```

This final matrix tells us the shortest distance between any two vertices. For example:

- Shortest path from vertex 2 to vertex 4: distance = 3 (via 2→3→4)
- Shortest path from vertex 3 to vertex 2: distance = 6 (via 3→4→1→2)
- Shortest path from vertex 4 to vertex 3: distance = 7 (via 4→1→2→3)

## Algorithm Summary

```
For each vertex k from 0 to n-1:
    For each vertex i from 0 to n-1:
        For each vertex j from 0 to n-1:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

## Time Complexity

- **O(n³)** - Three nested loops over all vertices

## Space Complexity

- **O(n²)** - Store the distance matrix

## When to Use Floyd-Warshall

- Need shortest paths between **all pairs** of vertices
- Graph is **dense** (many edges)
- Graph has **negative edge weights** (but no negative cycles)
- Matrix representation is natural for your problem
