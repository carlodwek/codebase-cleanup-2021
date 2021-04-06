
from random import choice

def determine_winner(c,u):

    """
    Compares the computer choice and user choice against a directory of outcomes and outputs a resultant message.

    Params:
        c (string), the computer's choice: either rock, paper or scissors
        u (string), the user's choice: either rock, paper or scissors

    Examples:
        determine_winner("rock", "scissors")
    """

    winners = {
    "rock":{
        "rock": None, # represents a tie
        "paper": "paper",
        "scissors": "rock",
    },
    "paper":{
        "rock": "paper",
        "paper": None, # represents a tie
        "scissors": "scissors",
    },
    "scissors":{
        "rock": "rock",
        "paper": "scissors",
        "scissors": None, # represents a tie
    },
    }
    winning_choice = winners[u][c]
    if winning_choice == u:
        out = "The user wins"
    elif winning_choice == c:
        out = "The computer wins"
    elif winning_choice is None:
        out = "It's a tie!"

    return out

#
# USER SELECTION
#
if __name__ == "__main__":
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    choices = ["rock", "paper", "scissors"]
    if u not in choices:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(choices)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    result = determine_winner(c,u)
    print(result)
