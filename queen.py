def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
            
        return True
    
    def backtrack(board, col, solutions):
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append(j)
            solutions.append(solution)
            return
        
        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(board, col + 1, solutions)
                board[row][col] = 0
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(board, 0, solutions)
    return solutions

def print_solutions(solutions, n):
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}:")
        for row in range(n):
            line = ""
            for col in range(n):
                if solution[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()

if __name__ == "__main__":
    # Taking input from the user for the number of queens (n)
    n = int(input("Enter the number of queens: "))
    
    solutions = solve_n_queens(n)
    print(f"Found {len(solutions)} solutions for {n}-Queens problem.")
    print_solutions(solutions[:3], n)
    if len(solutions) > 3:
        print(f"... and {len(solutions) - 3} more solutions.")

