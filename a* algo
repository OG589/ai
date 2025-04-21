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
    
    return None  # No path found

# Example usage with a grid-based graph
def grid_to_graph(grid):
    graph = {}
    height, width = len(grid), len(grid[0])
    
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1:  # 1 represents a wall
                continue
                
            pos = (x, y)
            graph[pos] = {}
            
            # Check the four adjacent cells
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] != 1:
                    graph[pos][(nx, ny)] = 1  # Weight of 1 for each step
    
    return graph

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Example grid (0 = open, 1 = wall)
example_grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def visualize_path(grid, path):
    visual = []
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[0])):
            if (x, y) == path[0]:
                row += "S "  # Start
            elif (x, y) == path[-1]:
                row += "G "  # Goal
            elif (x, y) in path:
                row += "* "  # Path
            elif grid[y][x] == 1:
                row += "# "  # Wall
            else:
                row += ". "  # Open
        visual.append(row)
    return visual

if __name__ == "__main__":
    # Create graph from grid
    graph = grid_to_graph(example_grid)
    
    # Define start and goal positions
    start = (0, 0)
    goal = (4, 4)
    
    # Find path
    path = astar(graph, start, goal, manhattan_distance)
    
    if path:
        print("Path found:", path)
        print("Path length:", len(path) - 1)
        print("Visualization:")
        for row in visualize_path(example_grid, path):
            print(row)
    else:
        print("No path found")
