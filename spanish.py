import random
import unidecode
from english import Get_Random_English
 
class Get_Random_Spanish(Get_Random_English):
 
    def random_word(self):
        # need to specify the encoding to read the file with accent marks and tildes
        with open(self.file, 'rt', encoding = 'utf-8') as f:
            words = f.read().splitlines()
            # removes accent marks and tildes
            for i in range(len(words)):
                words[i] = unidecode.unidecode(words[i])
        # selects a random word from the list
        word = random.choice(words)
        return word.upper()