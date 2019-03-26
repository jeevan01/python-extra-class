import random
number = random.randint(1,10)
tries=1

question=input("Do u want to play the game? [Y/N]")
if question == 'Y':
    guess = int(input("Have a guess:"))
    if guess<number:
        print("Guess Higher")
    elif guess>number:
        print("Guess Lower")
    else:
        print("You Win the game")
    while guess!=number:
        guess= int(input("Try Again"))
        if guess<number:
            print("Guess Higher")
        elif guess>number:
            print("Guess Lower")
        else:
            print("You Win the game")
            