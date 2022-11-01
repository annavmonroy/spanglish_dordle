import random
import spanish

class Spanish:

    def __init__(self, spanish):
        self.spanish = spanish
    
    def remove_accent(self):
        pass

    def random_word(self, word):
        with open(self.spanish) as f:
            self.word = f.read().splitlines()
        return random.choice(self.word)

# print(random_word('english.txt'))