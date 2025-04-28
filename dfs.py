# Depth First Search (DFS) for an undirected graph with user input

def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=' ')

    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {}

    # Input number of vertices and edges
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    # Input the edges
    print("Enter the edges (format: vertex1 vertex2):")
    for _ in range(num_edges):
        v1, v2 = input().split()

        # Since it's an undirected graph, add both connections
        graph.setdefault(v1, []).append(v2)
        graph.setdefault(v2, []).append(v1)

    # Input the starting vertex
    start_vertex = input("Enter the starting vertex for DFS: ")

    visited = set()

    print("Depth First Search traversal:")
    dfs(graph, start_vertex, visited)
