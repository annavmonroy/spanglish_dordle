import unidecode

# only checks if guess is a valid input
class Check_Guess:

    def __init_(self, guess, order, lowercase, uppercase, words):
        self.guess = guess
        self.order = order
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.words = words
        self.check = False

    def check_length(self):   # length = 5
        if len(self.guess) != 5:
            raise ValueError('Invalid guess')

    def check_letters(self):  # no symbols, accent marks, tildes, spaces, etc. # convert everything to uppercase
        for x in range(0, len(self.guess)):
            # converts the value in the string to it's unicode code 
            self.order = ord(self.guess[x])
            self.lowercase = range(97, 122)
            self.uppercase = range(65, 90)
        
            if self.order not in self.lowercase or self.uppercase:
                raise ValueError('Invalid guess')
    
    def check_word_bank(self):
        # checks if guess is in the english or spanish word bank
        self.guess = self.guess.lower()
        # checks english word bank
        with open('english.txt') as f:
            self.words = f.read().splitlines()
            if self.guess == self.words:
                self.check = True

        # checks spanish word bank
        with open('spanish.txt', 'rt', encoding = 'utf-8') as f:
            words = f.read().splitlines()
            for i in range(len(words)):
                words[i] = unidecode.unidecode(words[i])
            if self.guess == self.words:
                self.check = True
        
        if self.check == False:
            raise ValueError('Word not in word bank')

    def __str__(self):
        # converts guess to uppercase
        self.guess = self.guess.upper()
        return f'{self.guess}'