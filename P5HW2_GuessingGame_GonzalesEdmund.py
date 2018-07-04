# CTI - 110
# P5HW2: Random Number Guessing Game
# Gonzales, Edmund
# 7/4/18

import random

MIN = 1
MAX = 100

def main():
    
    choice = "y"
    
    while choice == "y":
        
        secretNumber = random.randint(MIN, MAX)
        play_game(secretNumber)
        choice = input("Do you wish to play again?")
          
    print("Thank you for playing.")
    

def play_game(secretNumber):

    count = 1 
    truth = secretNumber
    guess = int(input("Guess the secret number: "))
    
    while guess != truth:
        
        count = count + 1
        if guess < secretNumber:
            print("Too low, try agin.")
            guess = int(input("Guess the secret number: "))
        elif guess > secretNumber:
            print("Too high, try again.")
            guess = int(input("Guess the secret number: "))
    
    print("Congratulations, you have successfully guessed the secret number in",count,"tries.")


main()

    
            
        
        
    
