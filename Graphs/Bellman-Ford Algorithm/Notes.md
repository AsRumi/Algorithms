# Bellman-Ford Algorithm

## Overview

The Bellman-Ford Algorithm is a dynamic programming approach for finding the shortest path from a source vertex to all other vertices in a graph. Unlike Dijkstra's algorithm, Bellman-Ford can handle graphs with negative edge weights and can detect negative weight cycles.

## How It Works

1. **Initialization**: Set the distance to the source vertex as 0 and all other vertices to infinity.

2. **Relaxation**: Repeatedly relax all edges in the graph (V - 1) times, where V is the number of vertices. Relaxation means checking if the path through an edge offers a shorter distance than the current known distance.

3. **Relaxation Formula**: For an edge from u to v with weight w:
   ```
   if distance[u] + w < distance[v]:
       distance[v] = distance[u] + w
   ```

4. **Negative Cycle Detection**: After (V - 1) iterations, perform one more iteration. If any distance can still be improved, a negative weight cycle exists.

## Why V - 1 Iterations?

In a graph with V vertices, the longest possible shortest path without cycles has at most V - 1 edges. Therefore, V - 1 iterations guarantee that all shortest paths are found. If distances can still be reduced after V - 1 iterations, it indicates a negative cycle.

## Time Complexity

- General case: O(V × E) where V is vertices and E is edges
- For a graph with V vertices: O(V²) 
- For a fully connected graph: O(V³) (since E = V(V-1)/2)

## Example Traversal

Let's trace through the Bellman-Ford algorithm on the following graph:

**Edges**: 
```
[[1, 2, 6], [1, 3, 5], [1, 4, 5],
 [2, 5, -1],
 [3, 2, -2], [3, 5, 1],
 [4, 3, -2], [4, 6, -1],
 [5, 7, 3],
 [6, 7, 3]]
```

**Graph Structure**:
- Node 1 → Node 2 (weight 6), Node 3 (weight 5), Node 4 (weight 5)
- Node 2 → Node 5 (weight -1)
- Node 3 → Node 2 (weight -2), Node 5 (weight 1)
- Node 4 → Node 3 (weight -2), Node 6 (weight -1)
- Node 5 → Node 7 (weight 3)
- Node 6 → Node 7 (weight 3)

**Finding shortest paths from Node 1:**

### Step-by-Step Execution

**Initial State:**
```
{1: 0, 2: ∞, 3: ∞, 4: ∞, 5: ∞, 6: ∞, 7: ∞}
```

**Iteration 1**: Process all edges once
- Edge [1→2, 6]: distance[2] = min(∞, 0+6) = 6
- Edge [1→3, 5]: distance[3] = min(∞, 0+5) = 5
- Edge [1→4, 5]: distance[4] = min(∞, 0+5) = 5
- Edge [2→5, -1]: distance[5] = min(∞, 6-1) = 5
- Edge [3→2, -2]: distance[2] = min(6, 5-2) = 3
- Edge [3→5, 1]: distance[5] = min(5, 5+1) = 5
- Edge [4→3, -2]: distance[3] = min(5, 5-2) = 3
- Edge [4→6, -1]: distance[6] = min(∞, 5-1) = 4
- Edge [5→7, 3]: distance[7] = min(∞, 5+3) = 8
- Edge [6→7, 3]: distance[7] = min(8, 4+3) = 7

**After Iteration 1:**
```
{1: 0, 2: 3, 3: 3, 4: 5, 5: 5, 6: 4, 7: 7}
```

**Iteration 2**: Process all edges again
- Edge [1→2, 6]: distance[2] = min(3, 0+6) = 3 (no change)
- Edge [1→3, 5]: distance[3] = min(3, 0+5) = 3 (no change)
- Edge [1→4, 5]: distance[4] = min(5, 0+5) = 5 (no change)
- Edge [2→5, -1]: distance[5] = min(5, 3-1) = 2 ✓
- Edge [3→2, -2]: distance[2] = min(3, 3-2) = 1 ✓
- Edge [3→5, 1]: distance[5] = min(2, 3+1) = 2 (no change)
- Edge [4→3, -2]: distance[3] = min(3, 5-2) = 3 (no change)
- Edge [4→6, -1]: distance[6] = min(4, 5-1) = 4 (no change)
- Edge [5→7, 3]: distance[7] = min(7, 2+3) = 5 ✓
- Edge [6→7, 3]: distance[7] = min(5, 4+3) = 5 (no change)

**After Iteration 2:**
```
{1: 0, 2: 1, 3: 3, 4: 5, 5: 2, 6: 4, 7: 5}
```

**Iteration 3**: Process all edges again
- Edge [2→5, -1]: distance[5] = min(2, 1-1) = 0 ✓
- Edge [3→2, -2]: distance[2] = min(1, 3-2) = 1 (no change)
- Edge [5→7, 3]: distance[7] = min(5, 0+3) = 3 ✓
- All other edges: no changes

**After Iteration 3:**
```
{1: 0, 2: 1, 3: 3, 4: 5, 5: 0, 6: 4, 7: 3}
```

**Iterations 4, 5, 6**: No further improvements occur

### Final Shortest Paths from Node 1

- Node 1 → Node 1: Distance = 0, Path: [1]
- Node 1 → Node 2: Distance = 1, Path: [1, 3, 2]
- Node 1 → Node 3: Distance = 3, Path: [1, 4, 3]
- Node 1 → Node 4: Distance = 5, Path: [1, 4]
- Node 1 → Node 5: Distance = 0, Path: [1, 3, 2, 5]
- Node 1 → Node 6: Distance = 4, Path: [1, 4, 6]
- Node 1 → Node 7: Distance = 3, Path: [1, 3, 2, 5, 7]

### Negative Cycle Detection

After 6 iterations (V - 1 = 7 - 1 = 6), we perform one more check:
- Process all edges again
- If any distance improves, a negative cycle exists
- In this example, no improvements occur, so **no negative cycle is present**

## Key Observations

1. **Negative weights handled**: Notice that node 5 has a final distance of 0 from node 1, achieved through the path that includes negative weight edges.

2. **Multiple relaxations needed**: Some distances improved over multiple iterations (e.g., node 7 went from 8 → 7 → 5 → 3).

3. **Order independence**: Unlike Dijkstra's algorithm, Bellman-Ford processes all edges in each iteration, making it order-independent.

## Advantages over Dijkstra

- Works with negative edge weights
- Can detect negative cycles
- Simpler to implement

## Disadvantages

- Slower time complexity: O(V × E) vs Dijkstra's O((V + E) log V)
- Less efficient for graphs without negative weights