def solve_n_queens_branch_and_bound(row, n, column, left_diagonal, right_diagonal, board):
    if row == n:
        print_board(board, n)
        return

    for col in range(n):
        if column[col] or left_diagonal[row + col] or right_diagonal[row - col + n - 1]:
            continue

        board[row][col] = 1
        column[col] = left_diagonal[row + col] = right_diagonal[row - col + n - 1] = True

        solve_n_queens_branch_and_bound(row + 1, n, column, left_diagonal, right_diagonal, board)

        # Backtrack
        board[row][col] = 0
        column[col] = left_diagonal[row + col] = right_diagonal[row - col + n - 1] = False

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] else '.', end=' ')
        print()
    print()

def main():
    n = int(input("Enter the number of queens: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    column = [False] * n
    left_diagonal = [False] * (2 * n - 1)
    right_diagonal = [False] * (2 * n - 1)

    print("\nSolutions using Branch and Bound:\n")
    solve_n_queens_branch_and_bound(0, n, column, left_diagonal, right_diagonal, board)

if __name__ == "__main__":
    main()
