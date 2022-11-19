import random
 
class Get_Random_English:
 
    def __init__(self, filename):
        self.file = filename
 
    def random_word(self):
        with open(self.file) as f:
            words = f.read().splitlines()
        word = random.choice(words)
        return word.upper()