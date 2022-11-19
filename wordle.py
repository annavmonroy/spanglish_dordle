from valid_input import Valid_Input

class Wordle:
 
    def __init__(self, random): 
        self.random = random  
 
        # ANSI Escape Sequence for color coding and bolding
        self.correct = '\x1b[1m\x1b[92m'
        self.move = '\x1b[1m\x1b[35m'
        self.wrong = ''
        # When finished with a colour need to reset it back to normal text.
        self.reset = '\x1b[0m'
   
    def check_letters(self, random):
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
 
    def color_coding(self, random):
        # gives color coded word
        self.lst = []
        for letter, check in zip(self.guess, self.check_letters(self.random)):
            # check = every value in self.checked
            # letter = every letter in the guess
            # self.reset turns the bold off and color back to white after every letter (\x1b[0m)
            self.lst.append(f'{check}{letter}{self.reset}')
        # join converts lst to colored
        return ''.join(self.lst)

    def __str__(self):
        self.num = 1
        self.guess = None
 
        print('Play Wordle! ')
        # game keeps going until correct answer or runs out of guesses (7)
        while self.num < 7 and self.guess != self.random:
            self.guess = input(f'Guess {self.num}: ')

            # checks if guess is a valid input
            self.check_input = Valid_Input(self.guess)
            self.check_input = self.check_input.valid_input(self.check_input)
            if self.check_input == True:
                # converts input to uppercase
                self.guess = self.guess.upper()
                print('\t', self.color_coding(self.random))
                self.num += 1
            else:
                print(self.check_input)

        if self.guess == self.random:
            return 'You Win!'
        
        if self.num > 6:
            print('You ran out of guesses')
            return self.random