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

def print_adjacencyMatrix(matrix):
    for i in range(len(matrix)):
        print(f"\t{i + 1}", end = "")
    print()
    for i, row in enumerate(matrix):
        print(f"{i+1}|", end = "")
        for element in row:
            print(f"\t{element}", end = "")
        print()
        
def floyd_warshall(graph, vertices):
    
    initial_matrix = [[float('inf')] * vertices for _ in range(vertices)]
    
    # Find out the initial matrix simply as the distance from every node to every other node, infinity being the distance if the node cannot directly be reached from the current node.
    for i in range(vertices):
        for j in range(vertices):
            if i == j:
                initial_matrix[i][j] = 0
            else:
                if i + 1 in graph:
                    for neighbor, weight in graph[i + 1]:
                        initial_matrix[i][neighbor - 1] = weight
    
    dist = [row[:] for row in initial_matrix]
    
    for k in range(vertices): # For every node to be considered the intermediate node, modify the distances adjacency matrix
        for i in range(vertices):
            for j in range(vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) # Either the direct path is shorter, or the path going through current intermediate node

    print_adjacencyMatrix(dist)

edges = [[1, 2, 3], [1, 4, 7],
         [2, 1, 8], [2, 3, 2],
         [3, 4, 1], [3, 1, 5],
         [4, 1, 2]]

graph = create_weighted_graph(edges, True)
floyd_warshall(graph, 4)