def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_backtracking(board, row, n):
    if row == n:
        # Solution found
        print_board(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_backtracking(board, row + 1, n)
            board[row][col] = 0  # Backtrack

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] else '.', end=' ')
        print()
    print()

def main():
    n = int(input("Enter the number of queens: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    print("\nSolutions using Backtracking:\n")
    solve_n_queens_backtracking(board, 0, n)

if __name__ == "__main__":
    main()



