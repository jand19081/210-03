import random

class Secret():
    """An instance of secret.

        Attributes:
            _secret_word: The secret word.
    """

    def __init__(self):
        """An instance of the secret word."""
        words = ["car", "truck", "bed", "tent", "house", "bicycle", "picture", "computer",
        "cane", "fire", "couch", "blanket", "tree", "fireplace", "fan", "carpet", "table"]

        self._secret_word = random.choice(words)
        self._guess = []
        
        for letter in self._secret_word:
            self._guess.append("_")

    def check_geuss(self, letter_guess):
        """Checks if the letter guessed is in the secret word.
           If it is, it replaces the blank in guess and returns true.
           If not, then it returns false.
        """
        correct = False

        for i in range(len(self._secret_word)):
            if self._secret_word[i] == letter_guess:
                self._guess[i] = letter_guess
                correct = True

        return correct

    def get_guess(self):
        """Gets the guess as it stands."""
        guess = ""
        for i in range(len(self._guess)):
            guess += self._guess[i]

        return guess

    def get_secret_word(self):
        return self._secret_word