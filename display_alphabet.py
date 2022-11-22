class Display_Alphabet():

    def __init__(self, guess, random):
        self.guess = guess.upper()
        self.random = random.upper()
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # ANSI Escape Sequence for color coding and bolding
        self.correct = '\x1b[1m\x1b[92m' #green
        self.move = '\x1b[1m\x1b[33m'    #yellow
        self.used = '\x1b[1m\x1b[31m'     #red
        # When finished with a colour need to reset it back to normal text.
        self.reset = '\x1b[0m' 

    def check_letters_used(self, guess, random):
        self.green_letters = []
        self.yellow_letters = []
        self.red_letters = []
        # converts string of word to a list
        self.lst_random = list(self.random)
        self.checked = [''] *5
 
        # checks for correct letter in correct place
        for x, letter in enumerate(self.guess):
            if letter == self.random[x]:
                self.checked[x] = letter
                self.green_letters.append(letter)
                # Remove from list so it doesn't get checked again
                self.lst_random[x] = None
       
        # checks for correct letter in wrong place
        for x, letter in enumerate(self.guess):
            if self.checked[x] == '':
                if letter in self.lst_random:
                    self.checked[x] = letter
                    self.yellow_letters.append(letter)
                    # Remove from list so it doesn't get checked again
                    self.lst_random.remove(letter)
                else:
                    # letters that are not shared between the two words
                    self.checked[x] = letter
                    self.red_letters.append(letter)
        
        for letter in self.green_letters:
            # if statement is for double letters
            if letter in self.alphabet:
                x = self.alphabet.index(letter)
                self.alphabet[x] = f'{self.correct}{letter}{self.reset}'

        for letter in self.yellow_letters:
            # if statement is for double letters
            if letter in self.alphabet:
                x = self.alphabet.index(letter)
                self.alphabet[x] = f'{self.move}{letter}{self.reset}'

        for letter in self.red_letters:
            # if statement is for double letters
            if letter in self.alphabet:
                x = self.alphabet.index(letter)
                self.alphabet[x] = f'{self.used}{letter}{self.reset}'
        
        self.alphabet = ' '.join(self.alphabet)
        return self.alphabet