import random
piles = [1, 3, 5, 7]
def xor_sum(piles):
    #Calculate the XOR sum of the piles, which is used to determine the optimal move.
    xor_sum = 0
    for pile in piles:
        xor_sum ^= pile
    return xor_sum
def computer_move(piles):
#Given a list of piles, return the pile and number of stones to remove to ensure that the
#computer wins the game. The strategy is to always maintain an even XOR sum of the piles,
#which guarantees that there is always a winning move.
    xor = xor_sum(piles)
    if xor == 0:
      # If the XOR sum is already 0, remove a random number of stones
         pile = random.choice(range(len(piles)))
         move = random.choice(range(1, piles[pile] + 1))
         return pile, move
    else:
    # Find the highest bit in the XOR sum and remove stones from the pile
    # that has a 1 in that position
         highest_bit = 1
         while highest_bit <= xor:
           highest_bit <<= 1
         highest_bit >>= 1
         for pile, stones in enumerate(piles):
             if stones & highest_bit != 0:
                  return pile, stones - (stones ^ xor)
    # Should never get here
    return None
def play_game():
   # Play a game of Nim between the user and the computer. The user always goes first.
    player = 1
    while sum(piles) > 0:
        print(f"Piles: {piles}")
        if player == 1:
        # Player's turn
            while True:
                 pile = int(input("Player 1, which pile do you want to remove stones from? (1-4) "))
                 if pile < 1 or pile > 4:
                      print("Invalid pile. Please choose a valid pile.")
                      continue
                 move = int(input(f"How many stones do you want to remove from pile {pile}? "))
                 if move > piles[pile - 1]:
                     print("Invalid move. You cannot remove more stones than there are in the pile.")
                     continue
                 piles[pile - 1] -= move
                 break
            player = 2
        else:
        # Computer's turn
            pile, move = computer_move(piles)
            print(f"Player 2 removes {move} stones from pile {pile + 1}.")
            piles[pile] -= move
            player = 1
    # Game over
    if player == 1:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
play_game() 