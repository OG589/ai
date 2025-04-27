import sys

def prim(graph, n):
    selected = [False] * n
    edge_count = 0
    selected[0] = True
    
    print("Edge  \tWeight")
    while edge_count < n - 1:
        minimum = sys.maxsize
        x = 0
        y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j
                            
        print(f"{x}-{y}  \t{graph[x][y]}")
        selected[y] = True
        edge_count += 1

def take_user_input():
    n = int(input("Enter the number of vertices in the graph: "))
    
    # Create an adjacency matrix for the graph
    graph = []
    print(f"Enter the weights for the {n}x{n} adjacency matrix:")
    for i in range(n):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated values): ").strip().split()))
        graph.append(row)
    
    return graph, n

if __name__ == "__main__":
    graph, n = take_user_input()
    prim(graph, n)

