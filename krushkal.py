# Kruskal's Algorithm to find Minimum Spanning Tree (MST)

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            self.parent[u_root] = v_root

def kruskal(edges, n):
    # Sort edges based on weight
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(n)
    mst = []
    total_cost = 0

    print("Edge \tWeight")
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight
            print(f"{u}-{v} \t{weight}")

    print(f"Total cost of Minimum Spanning Tree: {total_cost}")

def take_user_input():
    n = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))

    edges = []
    print("Enter edges (format: vertex1 vertex2 weight):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    return edges, n

if __name__ == "__main__":
    edges, n = take_user_input()
    kruskal(edges, n)
