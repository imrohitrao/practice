def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Check row
            return True
        if all(board[j][i] == player for j in range(3)):  # Check column
            return True
    if all(board[i][i] == player for i in range(3)):  # Check main diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check anti-diagonal
        return True
    return False


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn.")

        # Get input from the player
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue

        # Update board
        board[row][col] = current_player
        print_board(board)

        # Check for win or draw
        if is_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # Switch turn
        turn += 1


if __name__ == "__main__":
    play_tic_tac_toe()
