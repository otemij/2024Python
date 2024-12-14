import random

num = random.randint(1,100)
print("The number is between 1 and 100 ")
guess = int(input("Enter in your guess: "))
if guess > 100 or guess < 1:
    print("invalid guess re-run the program")
    
while guess != num:
    if guess > num:
        guess = int(input("Lower. Guess again: "))
    elif guess < num:
        guess = int(input("Higher. Guess again: "))

print("You guessed it")
