class Display_Alphabet():
    """Displays the letters used in the game
    """

    def __init__(self, guesses_lst, random):
        """Initializes variables

        Args:
            guesses_lst (lst): user input in a list format
            random (str): random 5 letter word (in English or Spanish)
        """
        self.guesses_lst = guesses_lst
        self.random = random.upper()
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.alphabet2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # ANSI Escape Sequence for color coding and bolding
        self.correct = '\x1b[1m\x1b[92m' #green
        self.move = '\x1b[1m\x1b[33m'    #yellow
        self.used = '\x1b[1m\x1b[31m'     #red
        # When finished with a colour need to reset it back to normal text.
        self.reset = '\x1b[0m' 

    def check_letters_used(self, guesses_lst, random):
        """checks and displays letters used

        Args:
            guesses_lst (lst): user input in a list format
            random (str): random 5 letter word (in English or Spanish)

        Returns:
            str: alphabet with color coded letters
        """
        self.green_letters = []
        self.yellow_letters = []
        self.red_letters = []

        for guess in self.guesses_lst:
            self.guess = guess
            # converts string of word to a list
            self.lst_random = list(self.random)
            self.checked = [''] *5

            # checks for correct letter in correct place
            for x, letter in enumerate(self.guess):
                if letter == self.random[x]:
                    self.checked[x] = letter
                    self.green_letters.append(letter)

                    # letter should only be in one list at a time
                    if letter in self.yellow_letters:
                        self.yellow_letters.remove(letter)
                    elif letter in self.red_letters:
                        self.red_letters.remove(letter)

                    # Remove from list so it doesn't get checked again
                    self.lst_random[x] = None
       
            # checks for correct letter in wrong place
            for x, letter in enumerate(self.guess):
                if self.checked[x] == '':
                    if letter in self.lst_random:
                        self.checked[x] = letter
                        self.yellow_letters.append(letter)

                        # letter should only be in one list at a time
                        if letter in self.red_letters:
                            self.red_letters.remove(letter)

                        # Remove from list so it doesn't get checked again
                        self.lst_random.remove(letter)
                    else:
                        # letters that are not shared between the two words
                        self.checked[x] = letter
                        self.red_letters.append(letter)
            
            # resets a letter to the actual letter without the color
            for x, letter in enumerate(self.guess):
                x = self.alphabet2.index(letter)
                self.alphabet[x] = letter
        
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