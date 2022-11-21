class Letters_Used():

    def __init__(self, guess, random): 
        self.guess = guess.upper()
        self.random = random.upper()
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # ANSI Escape Sequence for color coding and bolding
        self.correct = '\x1b[1m\x1b[92m' #green
        self.move = '\x1b[1m\x1b[33m'    #yellow
        self.used = '\x1b[1m\x1b[31m'     #red
        self.wrong = ''
        # When finished with a colour need to reset it back to normal text.
        self.reset = '\x1b[0m' 
   
    def check_letters(self, guess, random):
        self.green_letters = []
        self.yellow_letters = []
        self.red_letters = []

        # converts string of random word to a list
        self.lst_random = list(self.random)
        # empty string to store results of checked letters
        self.checked = [''] * 5
        self.alphabet_checked = [''] * 26
 
        # checks for correct letter in correct place
        for x, letter in enumerate(self.guess):
            if letter == self.random[x]:
                self.checked[x] = self.correct
                self.green_letters.append(letter)
                # Remove from list so it doesn't get checked again
                self.lst_random[x] = None
       
        # checks for correct letter in wrong place
        for x, letter in enumerate(self.guess):
            if self.checked[x] == '':
                if letter in self.lst_random:
                    self.checked[x] = self.move
                    self.yellow_letters.append(letter)
                    # Remove from list so it doesn't get checked again
                    self.lst_random.remove(letter)
                else:
                    # letters that are not shared between the two words
                    self.checked[x] = self.wrong
                    self.red_letters.append(letter)

        for letter in self.green_letters:
            x = self.alphabet.index(letter)
            self.alphabet_checked[x] = self.correct

        for letter in self.yellow_letters:
            x = self.alphabet.index(letter)
            self.alphabet_checked[x] = self.move

        for letter in self.red_letters:
            x = self.alphabet.index(letter)
            self.alphabet_checked[x] = self.used

        print(f'{self.checked}\n{self.green_letters}\n{self.yellow_letters}\n{self.red_letters}\n{self.alphabet_checked}')
        self.color_coding = ['\x1b[1m\x1b[92m', '', '', '', '\x1b[1m\x1b[31m', '', '', '', '', '', '', '', '', '', '', '', '', '\x1b[1m\x1b[92m', '\x1b[1m\x1b[33m', '\x1b[1m\x1b[31m', '', '', '', '', '', '']
        self.color_coding2 = ['\x1b[1m\x1b[92m', '', '', '', '\x1b[1m\x1b[31m', '', '', '', '', '', '', '', '', '', '', '', '', '\x1b[1m\x1b[92m', '\x1b[1m\x1b[33m', '\x1b[1m\x1b[31m', '', '', '', '', '', '']
        print(self.alphabet)

        # gives color coded word
        self.lst = []
        for letter, check in zip(self.alphabet, self.color_coding2):
            # check = every value in self.checked
            # letter = every letter in the guess
            # self.reset turns the bold off and color back to white after every letter (\x1b[0m)
            print(check, letter, self.reset)
            self.lst.append(f'{check}{letter}{self.reset}')
        # join converts lst to colored
        print(self.lst)
        return ' '.join(self.lst)