import random
import unidecode

def random_word():
    # reads file with accent marks
    with open('spanish.txt', 'rt', encoding = 'utf-8') as f:
        words = f.read().splitlines()
        # removes accent marks and tildes
        for i in range(len(words)):
            words[i] = unidecode.unidecode(words[i])
    word = random.choice(words)
    return word.upper()

print(random_word())