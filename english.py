import random

def random_word():
    with open('english.txt') as f:
        words = f.read().splitlines()
    word = random.choice(words)
    return word.upper()

print(random_word())