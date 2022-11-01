import random
import english

def random_word(english):
    with open(english) as f:
        word = f.read().splitlines()
    return random.choice(word)

print(random_word('english.txt'))