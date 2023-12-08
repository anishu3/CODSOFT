# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import random

# Constants for representing the players and empty spaces on the board
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == EMPTY]

def minimax(board, depth, maximizing_player):
    if is_winner(board, PLAYER_X):
        return -1
    elif is_winner(board, PLAYER_O):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for row, col in get_empty_cells(board):
            board[row][col] = PLAYER_O
            eval = minimax(board, depth + 1, False)
            board[row][col] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in get_empty_cells(board):
            board[row][col] = PLAYER_X
            eval = minimax(board, depth + 1, True)
            board[row][col] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for row, col in get_empty_cells(board):
        board[row][col] = PLAYER_O
        eval = minimax(board, 0, False)
        board[row][col] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = (row, col)
    return best_move

def play_tic_tac_toe():
    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = PLAYER_X

    while True:
        print_board(board)

        if current_player == PLAYER_X:
            row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
            if board[row][col] != EMPTY:
                print("Cell already occupied. Try again.")
                continue
        else:
            print("AI is thinking...")
            row, col = get_best_move(board)

        board[row][col] = current_player

        if is_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    play_tic_tac_toe()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
