import random


### SKELETON FOR THE TIC TAC TOE GAME (defining a class and its methods)
### IT PRINTS THE BOARD
### PLAYER 1: USER CHOOSES
### PLAYER 2: COMPUTER RANDOMLY SELECTS A POS GIVEN THE CURRENT FREE SPACES



#Define the Class TicTacToe and its methods/functions
class TicTacToe:
    def __init__(self):
        # Define the variable board, " - " means empty spaces to choose, internally 0-8, for the user 1-9
        self.board = [" - ", " - ", " - ",
                      " - ", " - ", " - ",
                      " - ", " - ", " - "]
        
        # Use a variable to keep track of the current player
        self.current_player = " X "  # in this case the user is player 1 == " X "


    
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



    def get_computer_pos(self):
        """
        Function to randomly generate the computer choice given the current state, i.e. the random value generate will always be between the free spaces' indices
        """
        # Use a while loop to keep generating random positions until an empty one is found
        print("Computer's turn:")
        while True:
            player_pos = random.randint(0, 8)
            if self.board[player_pos] == " - ":
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
       
        
    # Function to check all possible winner combinations, if there is any successful combination in the board, the game has a winner and it is over    
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
    play_game()


#create object and run the game
#game = TicTacToe()
#TicTacToe.play_game()