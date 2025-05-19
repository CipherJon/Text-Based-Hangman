import random

class Data:
    words = [
        "hangman", "game", "python", "development", "code", "algorithm",
        "computer", "science", "programming", "software", "developer"
    ]

    @staticmethod
    def get_random_word():
        return random.choice(Data.words)