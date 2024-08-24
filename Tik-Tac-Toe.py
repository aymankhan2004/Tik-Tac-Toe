import random

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    """Function to print the current state of the board"""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(player):
    """Function to check if a player has won"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    """Function to check if the game is a draw"""
    return ' ' not in board

def take_turn(player):
    """Function for player to take their turn"""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("This spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid move. Please try again.")

def ai_move():
    """Function for AI to take its turn (ensuring a win or draw)"""
    # First, check if AI can win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner('O'):
                return
            board[i] = ' '  # Reset if it does not result in a win

    # Block the player if they are about to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner('X'):
                board[i] = 'O'
                return
            board[i] = ' '  # Reset if it does not result in a block

    # Otherwise, pick a random available spot
    available_moves = [i for i in range(9) if board[i] == ' ']
    move = random.choice(available_moves)
    board[move] = 'O'

def play_game():
    """Main function to play the game"""
    mode = input("Choose mode: 1 for Single Player (vs AI), 2 for Two Players: ")
    current_player = 'X'

    while True:
        print_board()

        if mode == '1' and current_player == 'O':
            ai_move()
        else:
            take_turn(current_player)

        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if is_draw():
            print_board()
            print("The game is a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()