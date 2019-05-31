"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

# variable for high score
global_high_score = None


def start_game(current_high_score):
    # Psuedo-code Hints
    # When the program starts, we want to:
    # ------------------------------------
    # 1. Display an intro/welcome message to the player.
    print("Welcome to PyGuess")
    print("==================")
    # 2. Store a random number as the answer/solution.
    answer = random.randint(1, 10)
    # generate variable to hold num of guesses
    num_guesses = 0
    # boolean to break loop
    guessed_correct = False
    # high score var
    high_score = current_high_score
    global global_high_score
    # Continuously prompt player to guess until correct
    while not guessed_correct:
        try:
            print("Guess a number between 1 and 10")
            guess = input()
            guess = int(guess)
        except ValueError:
            print("Please enter only integers between 1 and 10 (inclusive)")
            continue
        if guess > 10 or guess < 1:
            print("Please choose a number between 1 and 10 (inclusive)")
            continue
        num_guesses += 1
        if guess < answer:
            print("It's higher")
        elif guess > answer:
            print("It's lower")
        if guess == answer:
            print("You guessed correct! It took you {} tries!".format(num_guesses))
            print("Exiting game: Thanks for playing! :)")
            guessed_correct = True
            if high_score:
                if num_guesses < high_score:
                    high_score = num_guesses
                    global_high_score = high_score
            if not high_score:
                high_score = num_guesses
                global_high_score = high_score
            print("Current high score:", high_score)

    if guessed_correct:
        print("Would you like to play again? (Y/N)")
        decision = input()
        decision = str(decision)
        if (decision == 'Y') or (decision == 'y'):
            start_game(global_high_score)


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game(global_high_score)
