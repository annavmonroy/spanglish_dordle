import random
 
class Get_Random_English:
    """Generates a random five letter word in English
    """
 
    def __init__(self, filename):
        """Initializes file

        Args:
            filename (text file): list of 5 letter English words
        """
        self.file = filename
 
    def random_word(self):
        """Generates random word

        Returns:
            str: 5 letter English word
        """
        # reads and opens file
        with open(self.file) as f:
            words = f.read().splitlines()
        # selects a random word from the list
        word = random.choice(words)
        return word.upper()