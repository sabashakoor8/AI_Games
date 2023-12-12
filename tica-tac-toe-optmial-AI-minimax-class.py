import random


### SKELETON FOR THE TIC TAC TOE GAME (defining a class and its methods)
### IT PRINTS THE BOARD
### PLAYER 1: USER CHOOSES
### PLAYER 2: COMPUTER uses AI to never lose. Minimax algorithm for the optimal move.



#Define the Class TicTacToe and its methods/functions
class TicTacToe:
    def __init__(self):
        # Define the variable board, " - " means empty spaces to choose, internally 0-8, for the user 1-9
        self.board = [" - ", " - ", " - ",
                      " - ", " - ", " - ",
                      " - ", " - ", " - "]

        while True:
            user_wants_kick_off = input("Please inform 'Y' if you wish to start the game or 'N' if you wish the computer/AI starts:")
            if user_wants_kick_off.lower() == 'y':
                self.current_player = " X "
                break
            elif user_wants_kick_off.lower() == 'n':
                self.current_player = " O "
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")


    
    def display_board(self):
        """
        Function to display the current state of the board
        """
        print(" Tic Tac Toe ")
        print(self.board[0] + "|" + self.board[1] + "|" + self.board[2])
        print(self.board[3] + "|" + self.board[4] + "|" + self.board[5])
        print(self.board[6] + "|" + self.board[7] + "|" + self.board[8])
        print(" ")


        
    def play_game(self):
        """
        Function to start the game
        """
        self.display_board()

        while True:
            # Get the current player's position choice
            if self.current_player == " X ":
                player_pos = self.get_player_pos()
            else:
                player_pos = self.get_computer_pos()

            # Update the board with the current player's position
            self.board[player_pos] = self.current_player
            self.display_board()

            # Check for a winner or tie
            if self.check_winner(self.current_player):
                print("Congratulations! Player " + self.current_player + " wins!")
                break
            elif self.is_board_full():
                print("It's a tie!")
                break

            # Switch to the other player's turn
            self.current_player = self.switch_player(self.current_player)
        
      
        
    def get_player_pos(self):
        """
        Function to  get the current choice of player1
        """
        while True:
            try:
                # this line, we read the user's choice, but since the board index is between 0 and 8, and the user provide any number between 1 - 9, we subtract -1 for the current/real index in the board
                player_pos = int(input("Player 1, choose a free position in the board (1-9):")) - 1 
                # check if the current choice is free
                if player_pos in range(9):
                    if self.board[player_pos] == " - ":
                        return player_pos
                    else:
                        print("That position is already taken. Please choose another position.")
                else:
                    print("Please choose a position between 1 and 9.")
            except ValueError:
                print("Please enter a valid number.")


    # AI player, mart move from the computer
    def get_computer_pos(self):
        """
        Function to use the minimax function to select the optimal move.
        Returns the position for the computer to move (between 0-8).
        """
        print("Computer's turn:")
        _, player_pos = self.minimax(self.board, " O ")
        return player_pos


    # Function to check who the current player is, and then switch the turn
    def switch_player(self, current_player):
        """
        Function to check who the current player is, and then switch the turn
        """
        if current_player == " X ":
            return " O "
        else:
            return " X "
       
        
    # Function to check all possible winner combinations, if there is any successful combination on the board, the game has a winner and it is over    
    def check_winner(self, player):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
            (0, 4, 8), (2, 4, 6)            # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False
    
    
    
    #check if the board is full
    def is_board_full(self):
        # Use the "in" operator to check if any empty spaces are left on the board
        return all(pos != " - " for pos in self.board)
  
  
  
        
        #Function to Generate an AI move (optmial move given the current situation on the board)
    def minimax(self, board, player):
        """
        Minimax function to determine the best move for the computer.
        Returns the best score and best move.
        """
        # Define the player and opponent markers
        if player == " O ":
            opponent = " X "
        else:
            opponent = " O "
    
        # Define the base cases
        if self.check_winner(" O "):
            return (1, None)
        elif self.check_winner(" X "):
            return (-1, None)
        elif self.is_board_full():
            return (0, None)
    
        # Initialize the best_score and best_move variables
        if player == " O ":
            best_score = -float("inf")
        else:
            best_score = float("inf")
        best_move = None
    
        # Iterate through all possible moves and determine the best score and best move
        for i, pos in enumerate(board):
            if pos == " - ":
                board[i] = player
                score, _ = self.minimax(board, opponent)
                board[i] = " - "
    
                if player == " O ":
                    if score > best_score:
                        best_score = score
                        best_move = i
                else:
                    if score < best_score:
                        best_score = score
                        best_move = i
    
        return (best_score, best_move)



#create object and run the game
game = TicTacToe()
game.play_game()