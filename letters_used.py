import unidecode

class Letters_Used():

    def __init__(self, guess, random):
        self.guess = guess.upper()
        self.random = random.upper()
        self.alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        self.uppercase = range(65, 90)

        # ANSI Escape Sequence for color coding and bolding
        self.correct = '\x1b[1m\x1b[92m'
        self.move = '\x1b[1m\x1b[35m'
        self.wrong = ''
        # When finished with a colour need to reset it back to normal text.
        self.reset = '\x1b[0m' 

    def check_letters_used(self, guess, random):
        self.letters = []
        # converts string of random word to a list
        self.lst_random = list(self.random)
 
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
        return self.letters

    def display_letters_used(self, guess, random):
        pass