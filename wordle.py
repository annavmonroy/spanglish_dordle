class Wordle:
    """Figures out if the letters of guess are in the right place compared to the random word generated
    """
 
    def __init__(self, guess, random):
        """Initializes variables

        Args:
            guess (str): user input
            random (str): 5 letter random word (could be English or Spanish one)
        """
        self.guess = guess
        self.random = random  
 
        # ANSI Escape Sequence for color coding and bolding
        self.correct = '\x1b[1m\x1b[92m'
        self.move = '\x1b[1m\x1b[33m'
        self.wrong = ''
        # When finished with a colour need to reset it back to normal text.
        self.reset = '\x1b[0m'
   
    def check_letters(self, guess, random):
        """Identifies which letters are used, which are in the right place, and which are in the wrong place

        Args:
            guess (str): user input
            random (str): 5 letter random word (could be English or Spanish one)

        Returns:
            list: list with either color coding sequence or none, corresponding to the order of letters in guess
        """
        # converts string of random word to a list
        self.lst_random = list(self.random)
        # empty string to store results of checked letters
        self.checked = [''] * 5
 
        # checks for correct letter in correct place
        for x, letter in enumerate(self.guess):
            if letter == self.random[x]:
                self.checked[x] = self.correct
                # Remove from list so it doesn't get checked again
                self.lst_random[x] = None
       
        # checks for correct letter in wrong place
        for x, letter in enumerate(self.guess):
            if self.checked[x] == '':
                if letter in self.lst_random:
                    self.checked[x] = self.move
                    # Remove from list so it doesn't get checked again
                    self.lst_random.remove(letter)
                else:
                    # letters that are not shared between the two words
                    self.checked[x] = self.wrong
        return self.checked
 
    def show_colors(self, guess, random):
        """Puts the guess, color coding sequence, and reset together

        Args:
            guess (str): user input
            random (str): 5 letter random word (could be English or Spanish one)

        Returns:
            str: the guess with color coded letters
        """
        # gives color coded word
        self.lst = []
        for letter, check in zip(self.guess, self.check_letters(self.guess, self.random)):
            # check = every value in self.checked
            # letter = every letter in the guess
            # self.reset turns the bold off and color back to white after every letter (\x1b[0m)
            self.lst.append(f'{check}{letter}{self.reset}')
        # join converts lst to colored
        return ''.join(self.lst)