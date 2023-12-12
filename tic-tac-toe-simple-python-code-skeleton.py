

import random

### SKELETON FOR THE TIC TAC TOE GAME 
### IT PRINTS THE BOARD
### PLAYER 1: USER CHOOSES
### PLAYER 2: COMPUTER RANDOMLY SELECTS A POS GIVEN THE CURRENT FREE SPACES



# Define the variable board, " - " means empty spaces to choose, internally 0-8, for the user 1-9
board = [" - ", " - ", " - ",
         " - ", " - ", " - ",
         " - ", " - ", " - "]



# Function to display the current state of the board
def display_board():
    print(" Tic Tac Toe ")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print(" ")


# Function to start the game
def play_game():
    display_board()

    # Use a variable to keep track of the current player
    current_player = " X "  # in this case the user is player 1 == " X "

    while True:
        # Get the current player's position choice
        if current_player == " X ":
            player_pos = get_player_pos()
        else:
            player_pos = get_computer_pos()

        # Update the board with the current player's position
        board[player_pos] = current_player
        display_board()

        # Check for a winner or tie
        if check_winner(current_player):
            print("Congratulations! Player " + current_player + " wins!")
            break
        elif is_board_full():
            print("It's a tie!")
            break

        # Switch to the other player's turn
        current_player = switch_player(current_player)



# Function to  get the current choice of player1
def get_player_pos():
    while True:
        try:
            # this line, we read the user's choice, but since the board index is between 0 and 8, and the user provide any number between 1 - 9, we subtract -1 for the current/real index in the board
            player_pos = int(input("Player 1, choose a free position in the board (1-9):")) - 1 
            # check if the current choice is free
            if player_pos in range(9):
                if board[player_pos] == " - ":
                    return player_pos
                else:
                    print("That position is already taken. Please choose another position.")
            else:
                print("Please choose a position between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")



# Function to randomly generate the computer choice given the current state, i.e. the random value generate will always be between the free spaces' indices
def get_computer_pos():
    # Use a while loop to keep generating random positions until an empty one is found
    print("Computer's turn:")
    while True:
        player_pos = random.randint(0, 8)
        if board[player_pos] == " - ":
            return player_pos




# Function to check who the current player is, and then switch the turn
def switch_player(current_player):
    if current_player == " X ":
        return " O "
    else:
        return " X "



# Function to check all possible winner combinations, if there is any successful combination in the board, the game has a winner and it is over
def check_winner(player):
    # Define the indices of each possible winning combination
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)            # Diagonals
    ]
    # Check each winning combination for a win
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False



def is_board_full():
    # Use the "in" operator to check if any empty spaces are left on the board
    return all(pos != " - " for pos in board)


# start the game calling the function play_game()
play_game()
