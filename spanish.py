import random
import spanish

def random_word(spanish):
    # remove accent marks
    with open(spanish) as f:
        word = f.read().splitlines()
    return random.choice(word)

print(random_word('spanish.txt'))