import random
import os

PATH = os.path.join(os.path.dirname(__file__), "words.txt")


with open(PATH, mode='r') as file:
    words = file.readlines()
    word = random.choice(words)[:-1]

allowed_guesses = 8
guesses = []
play = True

while play:

    print(word)

    for letter in word:
        if letter.lower() not in guesses:
            print("_", end=" ")
        else:
            print(letter.lower(), end=" ")
    print(" ")

    guess = input(f"You have {allowed_guesses} guesses left. Pick a letter: ")

    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_guesses -= 1
        if allowed_guesses == 0:
            break

    play = False

    for letter in word:
        if letter.lower() not in guesses:
            play = True
        
if play:
    print(f"Game over! The word was '{word}'.")
else:
    print(f"You got it! The word was '{word}'.")