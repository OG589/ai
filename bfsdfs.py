import collections

def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])
    traversal_order = []
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    return traversal_order

def dfs(graph, root):
    visited = set()
    stack = [root]
    traversal_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return traversal_order

if __name__ == "__main__":
    graph = {}
    num_vertices = int(input("Enter number of vertices: "))

    for _ in range(num_vertices):
        vertex = input("\nEnter vertex name: ")
        neighbors = input(f"Enter neighbors of {vertex} separated by space (if none, press Enter): ").split()
        graph[vertex] = neighbors

    root = input("\nEnter starting vertex: ")

    bfs_order = bfs(graph, root)
    dfs_order = dfs(graph, root)

    print("\nBFS Traversal:", " -> ".join(bfs_order))
    print("DFS Traversal:", " -> ".join(dfs_order))

