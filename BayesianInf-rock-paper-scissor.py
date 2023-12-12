# simple Python Code for Bayesian Prediction for Rock, Paper, Scissor, Player1: User, Player2: Computer (randomly)



import random
from collections import Counter

def play_game():
    # Define the choices and corresponding outcomes
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    outcomes = {('r', 's'): 'Player 1 wins!', ('s', 'p'): 'Player 1 wins!', ('p', 'r'): 'Player 1 wins!', 
                ('s', 'r'): 'Player 2 wins!', ('p', 's'): 'Player 2 wins!', ('r', 'p'): 'Player 2 wins!'}
    
    # Get player 1's choice
    player1_choice = input("\nEnter your choice (r for rock, p for paper, s for scissors): ")
    while player1_choice not in choices:
        player1_choice = input("Invalid input. Enter your choice (r for rock, p for paper, s for scissors): ")
    
    # Generate player 2's choice randomly
    print("The computer randomly generates its choice.")
    player2_choice = random.choice(list(choices.keys()))
    print("Computer choses:", choices[player2_choice])
    
    # Determine the outcome and print the winner
    outcome = outcomes.get((player1_choice, player2_choice), "It's a tie!")
    print(outcome)
    
    return outcome
 
# Creare a histogram counting how many times each player won    
def update_counts(outcome, counts):
    # Update the counts based on the outcome
    if 'Player 1' in outcome:
        counts['p1_wins'] += 1
    elif 'Player 2' in outcome:
        counts['p2_wins'] += 1
    else:
        counts['ties'] += 1
    
    return counts


# Bayesian inference to predict the next winner
def get_bayesian_prediction(counts):
    # Compute the Bayesian prediction of the next winner
    total = sum(counts.values())
    p1_prior = counts['p1_wins'] / total
    p2_prior = counts['p2_wins'] / total
    tie_prior = counts['ties'] / total
    
    p1_likelihood = counts['p1_wins'] / (counts['p1_wins'] + counts['p2_wins'] + counts['ties'])
    p2_likelihood = counts['p2_wins'] / (counts['p1_wins'] + counts['p2_wins'] + counts['ties'])
    tie_likelihood = counts['ties'] / (counts['p1_wins'] + counts['p2_wins'] + counts['ties'])
    
    p1_posterior = (p1_likelihood * p1_prior) / (p1_likelihood * p1_prior + p2_likelihood * p2_prior + tie_likelihood * tie_prior)
    p2_posterior = (p2_likelihood * p2_prior) / (p1_likelihood * p1_prior + p2_likelihood * p2_prior + tie_likelihood * tie_prior)
    tie_posterior = 1 - p1_posterior - p2_posterior
    
    return p1_posterior, p2_posterior, tie_posterior
    

# Play the game
#define initial prior : uniform distribution
counts = {'p1_wins': 0.334, 'p2_wins': 0.33, 'ties': 0.33}
play_again = True
while play_again:
    # Print the initial probabilities
    total = sum(counts.values())

    
    # Play the game and update the counts
    outcome = play_game()
    counts = update_counts(outcome, counts)
    
    # Get the Bayesian prediction and print the updated probabilities
    p1_posterior, p2_posterior, tie_posterior = get_bayesian_prediction(counts)
    print("\nPredicition for next winner: Player 1 = {:.2f}, Player 2 = {:.2f}, Tie = {:.2f}".format(p1_posterior, p2_posterior, tie_posterior))
    
    # Ask if the user wants to play again
    play_again_input = input("Do you want to play again? (y/n): ")
    print("\n ")
    while play_again_input.lower() not in ('y', 'n'):
        play_again_input = input("Invalid input. Do you want to play again? (y/n): ")
    
    if play_again_input.lower() == 'n':
        play_again = False