#Write a program able to play the "Guess the number" - 
#game, where the number to be guessed is randomly chosen between 1 and 20. 
#This is how it should work when run in a terminal:
#Hello! What is your name? 
#KBTU 
#Well, KBTU, I am thinking of a number between 1 and 20. 
#Take a guess. 
#12 
#Your guess is too low. Take a guess. 
#16 
#Your guess is too low. 
#Take a guess. 
#19 
#Good job, KBTU! You guessed my number in 3 guesses!
import random

def play_guess_game():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    answer = random.randint(1, 20)
    num_guesses = 0
    while True:
        user_input = input("Take a guess: ")
        guess = int(user_input)
        num_guesses += 1

        if guess < answer:
            print("Your guess is too low. Take a guess.")
        elif guess > answer:
            print("Your guess is too high. Take a guess.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            return

if __name__ == "__main__":
    play_guess_game()