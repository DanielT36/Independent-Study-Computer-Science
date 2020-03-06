#Need to fix line 6, giving errors
#This program is a guessing game, where the user has to guess a randomly genrated 4-digit number.
#If the user guesses the right number in the right place, the user gains 1 "cow"
#If the user guesses the right number in the wrong place, they gain 1 "bull"
#Once the user the guesses the number the program displays the number of guesses.
import random

def Compare_Numbers(number, user_guess):
    cowbull = [0,0] 
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__=="__main__":
    playing = True 
    number = str(random.randint(0,9999)) 
    guesses = 0

    print("Let's play a game of Cowbull!") 
    
    while playing:
        user_guess = input("Give me your best guess! ")
        if user_guess == "exit":
            break
        cowbullcount = Compare_Numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break 
        else:
            print("Your guess is incorrect, try again.")