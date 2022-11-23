import random
 
class Get_Random_English:
 
    def __init__(self, filename):
        self.file = filename
 
    def random_word(self):
        # reads and opens file
        with open(self.file) as f:
            words = f.read().splitlines()
        # selects a random word from the list
        word = random.choice(words)
        return word.upper()