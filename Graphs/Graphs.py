def create_graph_directed(edges):
    graph = {}
    for edge in edges:
        u = edge[0]
        v = edge[1]
        if u not in graph:
            graph[u] = []
        if v not in graph[u]:
            graph[u].append(v)
    return graph

def create_undirected_graph(edges):
    graph = {}
    for edge in edges:
        u = edge[0]
        v = edge[1]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        if v not in graph[u]:
            graph[u].append(v)
        if u not in graph[v]:
            graph[v].append(u)
    return graph

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

def print_graph(graph, message = ""):
    print(message)
    for key, values in graph.items():
        print(F"{key} -> {values}")
        
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

def simple_dfs_traversal(graph, node):
    # Ready the stack, visited set, and distances dictionary for traversal.
    stack = [node]
    distances = {node: 0}
    visited = set()
    
    # Until there is a node you can visit:
    while stack:
        current_node = stack.pop() # Use that node
        if current_node in visited: # If already visited before, skip the node
            continue
        # Otherwise add it to visited set and process the node
        visited.add(current_node)
        if current_node in graph: # If the node has an outgoing edge
            for neighbor, weight in graph[current_node]: # For all its neighbors
                if neighbor in visited:
                    continue
                current_distance = weight + distances[current_node] # Calculate distance from the given node
                distances[neighbor] = current_distance # Set the distance of the neighbor to the calculated distance
                stack.append(neighbor) # Add the neighbor to be processed
                
    print("Using simple DFS, the traversal cost is as follows:")
    for node, distance in distances.items():
        print(f"Node {node} has cost {distance}.")
        
def bellman_ford(graph, node):
    return

# edges = [[1, 2], [2, 3], [3, 4], [4, 1]]
# edges_with_weights = [[1, 2, 5], [2, 3, 1], [3, 4, 2], [4, 1, 2]]
# directed_graph = create_graph_directed(edges)
# undirected_graph = create_undirected_graph(edges)
# weighted_graph = create_weighted_graph(edges_with_weights, directed = True)
# print_graph(weighted_graph, message="Weighted Graph")
# print_graph(directed_graph, message="Directed Graph")
# print_graph(undirected_graph, message="Undirected Graph")

edges1 = [[1, 2, 2], [1, 3, 4], [2, 3, 1], [2, 4, 5], [3, 5, 2], [5, 4, 1], [4, 6, 4], [5, 6, 1]]
graph1 = create_weighted_graph(edges1, directed = True)
print_graph(graph1, message="Graph for Dijkstra\'s traversal:")
distances = dijkstras(graph1, 1)
distances = simple_dfs_traversal(graph1, 1)