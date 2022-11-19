import unidecode
 
class Check_Guess:
 
    def __init__(self, guess):
        self.guess = guess
        self.check = False
 
    def check_length(self):   # length = 5
        if len(self.guess) != 5:
            return False
        else:
            return True
 
    def check_for_letters(self):  # no symbols, accent marks, tildes, spaces, etc. # convert everything to uppercase
        self.characters = []
        self.lowercase = range(97, 122)
        self.uppercase = range(65, 90)

        for x in range(0, len(self.guess)):
            # converts the value in the string to it's unicode code
            self.order = ord(self.guess[x])
            self.characters.append(self.order)

        for x in range(0, len(self.characters)):
            if self.characters[x] not in self.lowercase and self.characters[x] not in self.uppercase:
                return False
        return True
   
    def check_word_bank(self):
        # checks if guess is in the english or spanish word bank
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