import random

def print_board(board):
    print("\n")
    print("  0   1   2")
    for i, row in enumerate(board):
        print(i, " | ".join(row))
        if i < 2:
            print(" ---|---|--- ")
    print("\n")

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[0][col] != " " for row in range(3)):
            return board[0][col]
    
    if all(board[i][i] == board[0][0] and board[0][0] != " " for i in range(3)):
        return board[0][0]
    
    if all(board[i][2 - i] == board[0][2] and board[0][2] != " " for i in range(3)):
        return board[0][2]
    
    return None

def computer_move(board):
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_positions)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    turn = 0

    while turn < 9:
        print_board(board)

        if turn % 2 == 0:
            current_player = "X"
            print(f"Player {current_player}, enter your move (row and column, e.g., '0 1'): ")
            move = input().strip()
            try:
                row, col = map(int, move.split())
                if board[row][col] != " ":
                    print("Position already taken. Try again.")
                    continue
                board[row][col] = current_player
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers (0, 1, or 2) separated by a space.")
                continue
        else:
            current_player = "O"
            print("Computer is making a move...")
            row, col = computer_move(board)
            board[row][col] = current_player
            print(f"Computer placed 'O' in position ({row}, {col})")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return

        turn += 1

    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()