import random

def random_word(english):
    with open(english) as f:
        words = f.read().splitlines()
    word = random.choice(words)
    return word

print(random_word('english.txt'))