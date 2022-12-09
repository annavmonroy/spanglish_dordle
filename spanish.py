import random
import unidecode
from english import Get_Random_English
 
class Get_Random_Spanish(Get_Random_English):
    """Generates a random five letter word in Spanish 

    Args:
        Get_Random_English (class): generates 5 letter English word
    """
 
    def random_word(self):
        """generates random word

        Returns:
            str: 5 letter Spanish word
        """
        # need to specify the encoding to read the file with accent marks and tildes
        with open(self.file, 'rt', encoding = 'utf-8') as f:
            words = f.read().splitlines()
            # removes accent marks and tildes
            for i in range(len(words)):
                words[i] = unidecode.unidecode(words[i])
        # selects a random word from the list
        word = random.choice(words)
        return word.upper()