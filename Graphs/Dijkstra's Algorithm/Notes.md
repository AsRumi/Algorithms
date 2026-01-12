# Dijkstra's Algorithm

## Overview

Dijkstra's Algorithm is a graph algorithm used to find the shortest path from a source vertex to any given destination vertex in the graph. It is a greedy algorithm that works efficiently on graphs with non-negative edge weights.

## How It Works

1. **Initialization**: Set the source vertex as the current node with distance 0. All neighbors of the source have weights assigned as the cost to move from the current node to those nodes. All other unreachable nodes are assigned a distance of positive infinity.

2. **Greedy Selection**: At each step, select the unvisited node with the smallest distance globally.

3. **Relaxation**: After moving to the selected node, examine its neighbors and update their distances if a shorter path is found through the current node.

4. **Mark as Visited**: Once a node is processed, add it to the visited set and never revisit it.

5. **Repeat**: Continue until all reachable nodes have been visited or the destination is reached.

## Why Negative Weights Break the Algorithm

Dijkstra's algorithm fails with negative edge weights because it assumes that once a node is visited and its distance finalized, no shorter path to that node will be discovered later. With negative weights, a path explored later could reduce the distance to an already-visited node, violating this core assumption. The greedy choice of always selecting the minimum distance node only guarantees optimality when all weights are non-negative.

For graphs with negative weights, alternative algorithms like Bellman-Ford should be used.

## Example Traversal

Let's trace through Dijkstra's algorithm on the following graph:

**Edges**: `[[1, 2, 2], [1, 3, 4], [2, 3, 1], [2, 4, 5], [3, 5, 2], [5, 4, 1], [4, 6, 4], [5, 6, 1]]`

**Graph Structure**:
- Node 1 → Node 2 (weight 2), Node 3 (weight 4)
- Node 2 → Node 3 (weight 1), Node 4 (weight 5)
- Node 3 → Node 5 (weight 2)
- Node 5 → Node 4 (weight 1), Node 6 (weight 1)
- Node 4 → Node 6 (weight 4)

**Finding shortest paths from Node 1:**

### Step-by-Step Execution

| Step | Current Node | Distances | Visited | Notes |
|------|-------------|-----------|---------|-------|
| 0 | - | {1: 0, 2: ∞, 3: ∞, 4: ∞, 5: ∞, 6: ∞} | {} | Initial state |
| 1 | 1 | {1: 0, 2: 2, 3: 4, 4: ∞, 5: ∞, 6: ∞} | {1} | Explore neighbors of node 1 |
| 2 | 2 | {1: 0, 2: 2, 3: 3, 4: 7, 5: ∞, 6: ∞} | {1, 2} | From node 2: update node 3 (2+1=3 < 4), set node 4 to 7 |
| 3 | 3 | {1: 0, 2: 2, 3: 3, 4: 7, 5: 5, 6: ∞} | {1, 2, 3} | From node 3: set node 5 to 5 (3+2) |
| 4 | 5 | {1: 0, 2: 2, 3: 3, 4: 6, 5: 5, 6: 6} | {1, 2, 3, 5} | From node 5: update node 4 (5+1=6 < 7), set node 6 to 6 |
| 5 | 4 | {1: 0, 2: 2, 3: 3, 4: 6, 5: 5, 6: 6} | {1, 2, 3, 4, 5} | From node 4: no improvements (4+4=10 > 6 for node 6) |
| 6 | 6 | {1: 0, 2: 2, 3: 3, 4: 6, 5: 5, 6: 6} | {1, 2, 3, 4, 5, 6} | All nodes visited |

### Final Shortest Paths from Node 1

- Node 1 → Node 1: Distance = 0, Path: [1]
- Node 1 → Node 2: Distance = 2, Path: [1, 2]
- Node 1 → Node 3: Distance = 3, Path: [1, 2, 3]
- Node 1 → Node 4: Distance = 6, Path: [1, 2, 3, 5, 4]
- Node 1 → Node 5: Distance = 5, Path: [1, 2, 3, 5]
- Node 1 → Node 6: Distance = 6, Path: [1, 2, 3, 5, 6]

## Time Complexity

- With a binary heap: O((V + E) log V)
- With a Fibonacci heap: O(E + V log V)
- With an array: O(V²)

Where V is the number of vertices and E is the number of edges.