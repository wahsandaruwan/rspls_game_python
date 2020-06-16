"""Iplementing Rock, Spock, Paper, Lizard, Scissors Practice Project
    One popular five-weapon expansion is "rock paper scissors Spock lizard", invented by Sam Kass and Karen Bryla,[89] which adds "Spock" and "lizard" to the standard three choices. "Spock" is signified with the Star Trek Vulcan salute, while "lizard" is shown by forming the hand into a sock-puppet-like mouth. Spock smashes scissors and vaporizes rock; he is poisoned by lizard and disproved by paper. Lizard poisons Spock and eats paper; it is crushed by rock and decapitated by scissors. This variant was mentioned in a 2005 article in The Times of London[90] and was later the subject of an episode of the American sitcom The Big Bang Theory in 2008.
"""
# For random generate a random number using given range
from random import randrange as ranNum

def name_to_number(name):
    """Take string name as input (rock-spock-paper-lizard-scissor) and returns integer (0-1-2-3-4)
    """    
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissor":
        return 4
    else:
        return "Error"


def number_to_name(number):
    """Take integer number as input (0-1-2-3-4) and returns string (rock-spock-paper-lizard-scissor)
    """  
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissor"
    else:
        return "Error"


def rpsls(player_choice):
    print("")
    print("Player Choice : " + player_choice.lower())
    # Get number according to player choice
    player_number = name_to_number(player_choice.lower())
    
    # Get random number for computer choice
    comp_number = ranNum(0,5) # 0,1,2,3,4
    # Get computer choice
    comp_choice = number_to_name(comp_number)
    print("Computer Choice : " + comp_choice)

    # Determine the winner using simple arithmetic and modulor
    winner = (player_number - comp_number) % 5 # Ex : -3 % 5 ==> -3 -(floor(-3/5) * 5) | floor gives min value
    # If Difference of ((player_number - comp_number) % 5) is equal to 1 or 2 then player wins, if result is equal to 3 or 4 then computer wins
    
    if (winner < 3) and (winner > 0):
        print("Player Wins!")
    elif winner == 0:
        print("Draw")
    else:
        print("Computer Wins!")

# Start : Calling
rpsls("rock")




