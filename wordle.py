class Wordle:
 
    def __init__(self, guess, random): 
        self.guess = guess
        self.random = random  
 
        # ANSI Escape Sequence for color coding and bolding
        self.correct = '\x1b[1m\x1b[92m'
        self.move = '\x1b[1m\x1b[33m'
        self.wrong = ''
        # When finished with a colour need to reset it back to normal text.
        self.reset = '\x1b[0m'
   
    def check_letters(self, guess, random):
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
        # gives color coded word
        self.lst = []
        for letter, check in zip(self.guess, self.check_letters(self.guess, self.random)):
            # check = every value in self.checked
            # letter = every letter in the guess
            # self.reset turns the bold off and color back to white after every letter (\x1b[0m)
            self.lst.append(f'{check}{letter}{self.reset}')
        # join converts lst to colored
        return ''.join(self.lst)