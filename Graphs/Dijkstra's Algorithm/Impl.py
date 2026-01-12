def create_weighted_graph(edges, directed = False):
    graph = {}
    for edge in edges:
        u = edge[0]
        v = edge[1]
        weight = edge[2]
        if u not in graph:
            graph[u] = []
        graph[u].append((v, weight))
        if not directed:
            if v not in graph:
                graph[v] = []
            graph[v].append((u, weight))
    return graph

def dijkstras(graph, node, distances = None):
    # Use a priority queue to calculate distances, since you greedily select the next shortest route
    # Set up the distances hashmap, priority queue, and the set of visited nodes
    import heapq
    distances = {node: 0}
    pq = [(0, node)]
    visited = set()
    
    # While there are nodes you can visit
    while pq:
        current_dist, current_node = heapq.heappop(pq) # Fetch the current node to process
        if current_node in visited: # Skip it if it already has been visited
            continue
        visited.add(current_node)
        if current_node in graph: # If the node has an outgoing edge in the graph
            for neighbor, weight in graph[current_node]:
                if neighbor in visited:
                    continue
                new_dist = current_dist + weight # New distance is calculated as the weight and the distance to reach the node before the current node
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor)) # Push the neighbor into a priority heap, which bubbles the node all the way up the heap to its correct position based on its distance
    
    for node, distance in distances.items():
        print(f"Node {node} has shortest distance {distance}.")
    return distances


edges1 = [[1, 2, 2], [1, 3, 4], [2, 3, 1], [2, 4, 5], [3, 5, 2], [5, 4, 1], [4, 6, 4], [5, 6, 1]]
graph1 = create_weighted_graph(edges1, directed = True)
distances = dijkstras(graph1, 1)