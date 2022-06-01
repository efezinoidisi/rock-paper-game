import random

#this function welcomes the user and introduces how to play the game
def welcome():
    print("WELCOME TO THIS SIMPLE ROCK-PAPER-SCISSORS GAME")
    print("-------------------------------------------------------------------------------------------------------")
    print("Here are the rules: You are playing against the computer")
    print("Rock beats scissors, scissors beats paper and paper beats rock")
    print("you can only choose one of rock,paper or scissors")
    print("R for rock  P for paper S for scissors")
    print("-------------------------------------------------------------------------------------------------------")
    print("Are you ready? Lets Play!")

#this function accepts the users gameplay and checks if it is valid or not
def validate_user():
    while True:
        print("")
        user_input=input("What will you play?r,p or s: ")
        user_input = user_input.upper()
        if user_input == "R" or user_input == "P" or user_input == "S":
            return user_input
        else:
            print("Invalid input, try again!")

#this functions selects from a random list the cpu's choice
def cpu_choice():
    game_options = ["R","P","S"]
    return random.choice(game_options)

    
#this function compares the user and cpu choices and decides the winner
def winner_decision(user,cpu):
    while True:
        print("Player(",user,") : CPU(",cpu,")")
        if (user == "R") and (cpu == "P"):
            return "cpu"
        elif (user == "R") and (cpu == "S"):
            return "player"
        elif (user== "P") and (cpu == "R"):
            return "player"
        elif (user == "P") and (cpu == "S"):
            return "cpu"
        elif (user == "S") and (cpu == "R"):
            return "cpu"
        elif (user == "S") and (cpu == "P"):
            return "player"
        else:
            print("Tie! Try Again")
            user = validate_user()
            cpu = cpu_choice()
 
#this function displays the winner of the game
def winner_result(result):
    if result == "cpu":
        print("Computer Wins!")
    else:
        print("Player Wins!")
    print("Game Over!")
        
        
#main program block starts here
welcome()
user_choice = validate_user()
cpu = cpu_choice()
result = winner_decision(user_choice,cpu)
winner = winner_result(result)
