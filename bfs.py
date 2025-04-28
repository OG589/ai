from collections import deque

# Recursive BFS function
def bfs_recursive(graph, queue, visited):
    if not queue:
        return

    # Dequeue the first vertex
    vertex = queue.popleft()
    print(vertex, end=' ')

    # Visit all neighbors
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    # Recursive call for the next vertex in queue
    bfs_recursive(graph, queue, visited)

# Main function
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
    start_vertex = input("Enter the starting vertex for BFS: ")

    visited = set()
    queue = deque()

    # Initialize BFS
    visited.add(start_vertex)
    queue.append(start_vertex)

    print("Breadth First Search traversal:")
    bfs_recursive(graph, queue, visited)
