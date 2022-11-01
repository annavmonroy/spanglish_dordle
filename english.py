import random
import english

class English:

    def __init__(self, english):
        self.english = english

    def random_word(self, word):
        with open(self.english) as f:
            self.word = f.read().splitlines()
        return random.choice(self.word)

# print(random_word('english.txt'))