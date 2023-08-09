import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempt = 10
    #print("You have 10 attempts remaining to guess the number.")
elif difficulty == "hard":
    attempt = 5
    #print("You have 5 attempts remaining to guess the number.")

my_number = random.randint(1, 100)
#guess = int(input("Make a guess: "))
correct = False


def compare():
    if my_number > guess:
        print("Too low.")
        if attempt > 1:
            print("Guess again.")
        return attempt - 1
    elif my_number < guess:
        print("Too high.")
        if attempt > 1:
            print("Guess again.")
        return attempt - 1
    else:
        global correct
        correct = True
        print(f"You got it! The answer was {guess}.")
        # return correct = True


for n in range(attempt):
    while not correct:
        if attempt > 0:
            print(
                f"You have {attempt} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            attempt = compare()
            # print(
            # f"You have {attempt} attempts remaining to guess the number.")
            # guess = int(input("Make a guess: "))
        else:
            print("You've out of your guesses. You lose!")
            correct = True
