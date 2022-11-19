import random
import unidecode
from english import Get_Random_English
 
class Get_Random_Spanish(Get_Random_English):
 
    def random_word(self):
        # reads file with accent marks
        with open(self.file, 'rt', encoding = 'utf-8') as f:
            words = f.read().splitlines()
            # removes accent marks and tildes
            for i in range(len(words)):
                words[i] = unidecode.unidecode(words[i])
        word = random.choice(words)
        return word.upper()