import random
 
class Get_Random_English:
 
    def __init__(self, filename):
        self.file = filename
 
    def random_word(self):
        with open(self.file) as f:
            words = f.read().splitlines()
        word = random.choice(words)
        return word.upper()
 
#first_word = Get_Random_English('english.txt')
#print(first_word.random_word())