import heapq

def astar(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    open_set_hash = {start}
    
    while open_set:
        current_f_score, current = heapq.heappop(open_set)
        open_set_hash.remove(current)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                
                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    open_set_hash.add(neighbor)
    
    return None

def grid_to_graph(grid):
    graph = {}
    height, width = len(grid), len(grid[0])
    
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1:
                continue
                
            pos = (x, y)
            graph[pos] = {}
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] != 1:
                    graph[pos][(nx, ny)] = 1
    
    return graph

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def visualize_path(grid, path=None):
    """Visualizes the grid and optional path."""
    if path is None:
        path = []
    visual = []
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[0])):
            if path and (x, y) == path[0]:
                row += "S "  # Start
            elif path and (x, y) == path[-1]:
                row += "G "  # Goal
            elif path and (x, y) in path:
                row += "* "  # Path
            elif grid[y][x] == 1:
                row += "# "  # Wall
            else:
                row += ". "  # Open space
        visual.append(row)
    return visual

def take_user_input():
    height = int(input("Enter grid height: "))
    width = int(input("Enter grid width: "))
    
    # Initialize grid with open spaces (0)
    grid = [[0 for _ in range(width)] for _ in range(height)]
    
    num_walls = int(input("\nHow many walls do you want to place? "))
    print(f"\nEnter {num_walls} wall positions (x y) one by one:")

    placed_walls = 0
    while placed_walls < num_walls:
        x, y = map(int, input(f"Wall {placed_walls + 1}: ").strip().split())
        if 0 <= x < width and 0 <= y < height and grid[y][x] == 0:
            grid[y][x] = 1
            placed_walls += 1
        else:
            print("Invalid position or wall already placed. Try again.")
    
    print("\nWalls placed successfully!\n")
    print("Current Grid:")
    for row in visualize_path(grid):
        print(row)
    
    while True:
        start_x, start_y = map(int, input("\nEnter start position (x y): ").strip().split())
        if 0 <= start_x < width and 0 <= start_y < height and grid[start_y][start_x] == 0:
            start = (start_x, start_y)
            break
        else:
            print("Invalid start position! It must be inside grid and not on a wall.")
    
    while True:
        goal_x, goal_y = map(int, input("Enter goal position (x y): ").strip().split())
        if 0 <= goal_x < width and 0 <= goal_y < height and grid[goal_y][goal_x] == 0:
            goal = (goal_x, goal_y)
            break
        else:
            print("Invalid goal position! It must be inside grid and not on a wall.")
    
    return grid, start, goal

if __name__ == "__main__":
    grid, start, goal = take_user_input()
    
    graph = grid_to_graph(grid)
    
    path = astar(graph, start, goal, manhattan_distance)
    
    if path:
        print("\nPath found:", path)
        print("Path length:", len(path) - 1)
        print("\nVisualization:")
        for row in visualize_path(grid, path):
            print(row)
    else:
        print("\nNo path found")











import heapq
def a_star_algorithm(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, [start]))  # (f(estimated), g(total), current, path)
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current == goal:
            print("Path found:", ' → '.join(path))
            print("Total cost:", g)
            return

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                total_cost = g + cost
                estimated_cost = total_cost + heuristics[neighbor]
                heapq.heappush(open_list, (estimated_cost, total_cost, neighbor, path + [neighbor]))

    print("No path found.")

graph = {}
nodes = set()
n = int(input("Enter number of edges: "))
for i in range(n):
    u, v, cost = input("Enter edge (u v cost): ").split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))  # Since it's undirected (optional)
    nodes.update([u, v])

heuristics = {}
print("Enter heuristic values for each node:")
for node in nodes:
    heuristics[node] = int(input(f"Heuristic for {node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

a_star_algorithm(graph, heuristics, start, goal)



# Enter number of edges: 6
# Enter edges in the format 'u v cost' (e.g., A B 4):
# A B 1
# A C 4
# B D 2
# C D 5
# B E 3
# D E 1

# Enter heuristic (estimated cost to goal) for each node:
# Heuristic for A: 7
# Heuristic for B: 6
# Heuristic for C: 5
# Heuristic for D: 3
# Heuristic for E: 0

# Enter start node: A
# Enter goal node: E
