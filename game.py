from data import Data
import random
import data
import random
import data
import random

class Game:
    def __init__(self):
        self.words = data.words
        self.word = random.choice(self.words)
        self.guesses = set()
        self.lives = 6

    def start(self, player_name):
        print(f"Welcome to Hangman, {player_name}!")
        while self.lives > 0 and not all(letter in self.guesses for letter in self.word):
            print("Word:", " ".join(["_" if letter not in self.guesses else letter for letter in self.word]))
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetic character.")
                continue
            if guess in self.guesses:
                print(f"You already guessed '{guess}'. Try again.")
                continue
            self.guesses.add(guess)
            if guess in self.word:
                print(f"Correct! '{guess}' is in the word.")
            else:
                print(f"Incorrect! '{guess}' is not in the word. You lose a life.")
                self.lives -= 1
        if not all(letter in self.guesses for letter in self.word):
            print(f"You lost! The word was '{self.word}'.")
        else:
            print(f"Congratulations, {player_name}! You won!")

if __name__ == "__main__":
    game = Game()
    game.start(input("Enter your name: "))