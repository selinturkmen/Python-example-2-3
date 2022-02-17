import random
import math

def get_user_choice():
    """
    This function should:
        (1) Print the "It's time to play" message.
        (2) Ask for user's choice (0, 1, 2, -1).
        (3) Return the user's choice as an integer.
    Make sure to have a return statement!
    """
    n = input("User's choice: ")
    return n

def get_computer_choice():
    """ 
    This function should return an integer which corresponds to the computer's
    random choice (0, 1 or 2).
    Make sure to have a return statement!
    """
    i= random.randint(0,2)
    return i


def main():
    """
    Rock-Paper-Scissors program
    """
    print("Welcome to Rock-Paper-Scissors! My KU ID is: sturkmen20")
    print("It's time to play! Enter 0 for rock, 1 for paper, 2 for scissors, -1 to quit.")

    get_computer_choice()
    
    while  get_user_choice()!= -1:
     comp_score=0
     user_score=0   
     if get_computer_choice()==0 and get_user_choice()== 0:
        print("It's a tie! Both players chose rock.")
        print("Current score:", user_score, comp_score, "Computer")
     if get_computer_choice()==1 and get_user_choice()== 0:
        comp_score = comp_score +1
        print("Computer wins! Paper beats rock.")
        print("Current score:", user_score, comp_score, "Computer")
     if  get_computer_choice()==2 and get_user_choice()== 0:
         user_score = user_score +1
         print("User wins! Rock beats scissor.")
         print("Current score:", user_score, comp_score, "Computer")
     if get_computer_choice()== 0 and get_user_choice()== 1:
         user_score= user_score +1
         print("User wins! Paper beats rock.")
         print("Current score:", user_score, comp_score, "Computer")
     if get_computer_choice()== 1 and get_user_choice()==1:
         print("It's a tie! Both players chose paper.")
         print("Current score:", user_score, comp_score, "Computer")
     if get_computer_choice()==2 and get_user_choice()== 1:
         comp_score = comp_score +1
         print("Computer wins! Scissor beats paper.")
         print("Current score:", user_score, comp_score, "Computer")
     if get_computer_choice()==0 and get_user_choice()== 2:
        comp_score = comp_score +1
        print("Computer wins! Rock beats scissor.")
        print("Current score:", user_score, comp_score, "Computer")
     if get_computer_choice()==1 and get_user_choice()== 2:
        comp_score = comp_score +1
        print("Computer wins! Scissor beats paper.")
        print("Current score:", user_score, comp_score, "Computer")
     if get_computer_choice()==2 and get_user_choice()== 2:
         print("It's a tie! Both players chose scissor.")
         print("Current score:", user_score, comp_score, "Computer")
    print("Game has ended. Goodbye!")
    

    
    
    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()