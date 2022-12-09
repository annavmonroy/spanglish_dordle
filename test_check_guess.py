import unidecode
 
class Check_Guess:
    """Checks user input against sevral parameters
    """

    def __init__(self, guess):
        """Initializes variable

        Args:
            guess (str): user input
        """
        self.guess = guess
        self.check = False
 
    def check_length(self):
        """Checks input has length of 5

        Returns:
            boolean: If lenth 5 then True, else False
        """
        if len(self.guess) != 5:
            return False
        else:
            return True
 
    def check_for_letters(self):
        """Checks all characters in input are letters

        Returns:
            boolean: If all characters are letters then True, else False
        """
        # no symbols, accent marks, tildes, spaces, etc.
        self.characters = []
        # ascii range for lowercase and uppercase letters
        self.lowercase = range(97, 122)
        self.uppercase = range(65, 90)

        # makes a list of all unidecode codes for every character
        for x in range(0, len(self.guess)):
            # converts the value in the string to it's unicode code
            self.order = ord(self.guess[x])
            self.characters.append(self.order)

        # checks unidecodes are within ascii ranges for upper or lowercase letters
        for x in range(0, len(self.characters)):
            if self.characters[x] not in self.lowercase and self.characters[x] not in self.uppercase:
                return False
        return True
   
    def check_word_bank(self):
        """Checks input is in either the English or Spanish word bank

        Returns:
            boolean: If input is in either word bank then True, else False
        """
        # converts guess to lowercase to compare with lowercase words in word bank
        self.guess = self.guess.lower()

        # checks english word bank
        with open('english.txt') as f:
            self.words = f.read().splitlines()
            if self.guess in self.words:
                self.check = True
 
        # checks spanish word bank
        with open('spanish.txt', 'rt', encoding = 'utf-8') as f:
            self.words = f.read().splitlines()
            for i in range(len(self.words)):
                self.words[i] = unidecode.unidecode(self.words[i])
            if self.guess in self.words:
                self.check = True
       
        if self.check == False:
            return False
        else:
            return True