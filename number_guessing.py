# here I welcome the users to play the game
print("Welcome to the Number guessing game")
print ("Here you can win the game by guessing the number")

# import is used here to import random (which is a module)
import random
# we uses randint and ranges inside it  to generate a random number 

number = random.randint(1,100)
guess = 0
attempts=0 
# we uses loop here until the number is correct 
while guess!= number :
    guess= int(input("enter your guess :", ))
    # the attempts keeps on adding if the guesses is incorrect
    attempts+=1
    if (guess < number):
        print("guess higher")
    elif (guess > number):
       print("guess lower")
    else :
     print ("you won in", attempts,"attempts")
     print ("Thanks for playing this game")

    
