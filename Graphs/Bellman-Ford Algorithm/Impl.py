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

def bellman_ford(graph : dict, node : int, vertices : int, distances = {}):
    
    # A helper function to create a list edges from the given graph in the format [node, neighbor, weight]
    def edge_creator(graph):
        edges = []
        for key, values in graph.items():
            for neighbor, weight in values:
                edges.append([key, neighbor, weight])
        return edges
    
    edges = edge_creator(graph) # Collect all the edges first
    distances = {node: 0}
    negative_cycle = False 
    
    # Total number of vertices - 1 times
    for _ in range(vertices - 1):
        for node, neighbor, weight in edges: # For every edge in the graph:
            # Check if the edge leads to a node whose weight can be relaxed
            if (node in distances) and (distances[node] + weight < distances.get(neighbor, float('inf'))):
                distances[neighbor] = distances[node] + weight
                
    # Repeat the process one more time to see if weights can further be reduced, indicating the presence of a negative weight cycle
    for node, neighbor, weight in edges:
        if distances[node] + weight < distances.get(neighbor, float('inf')):
            negative_cycle = True
            break
        
    return distances, negative_cycle

edges1 = [[1, 2, 2], [1, 3, 4], [2, 3, 1], [2, 4, 5], [3, 5, 2], [5, 4, 1], [4, 6, 4], [5, 6, 1]]
graph1 = create_weighted_graph(edges1, directed = True)
distances, negative_cycle = bellman_ford(graph1, 1, 6)
# print(distances, negative_cycle)

edges2 = [[1, 2, 6], [1, 3, 5], [1, 4, 5],
          [2, 5, -1],
          [3, 2, -2], [3, 5, 1],
          [4, 3, -2], [4, 6, -1],
          [5, 7, 3],
          [6, 7, 3]]
graph2 = create_weighted_graph(edges2, directed = True)
distances, negative_cycle = bellman_ford(graph2, 1, 7)
print(distances, negative_cycle)