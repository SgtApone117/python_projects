import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:- "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high")
    print(f"Yay, You win. You guessed the correct random number i.e. {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        guess = random.randint(1,x)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C):- ").lower()
        if feedback == "h":
            high = high-1
        elif feedback == "l":
            low = low+1
    print(f"Yay, You win. You guessed the correct random number i.e. {guess}")
# guess(10)
# computer_guess(10)