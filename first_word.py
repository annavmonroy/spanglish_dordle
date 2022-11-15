# import the random word and the guess input
class English_Wordle:
 
    def __init__(self, guess, random):
        self.guess = guess    # import random english word
        self.random = random   # import user's guess
 
        # ANSI Escape Sequence for color coding and bolding
        self.correct = '\033[1m\033[92m'
        self.move = '\033[1m\033[35m'
        self.wrong = ''
        # When finished with a colour need to reset it back to normal text.
        self.reset = '\033[0m'
   
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
 
    def color_coding(self, guess, random):
        # gives color coded word
        self.lst = []
        for letter, check in zip(self.guess, self.check_letters(self.random, self.guess)):
            self.lst.append(f"{check}{letter}{self.reset}")
        return ''.join(self.lst)

    def __str__(self):
        self.num = 0
        self.guess = None
 
        print(f'Play Wordle! ')
        # game keeps going until correct answer or runs out of guesses (7)
        while self.num < 7 and self.guess != self.random:
            self.num += 1
            self.guess = input(f'Guess {self.num}: ')
            # converts input to uppercase
            self.guess = self.guess.upper()
            print(f'         {self.color_coding(self.random, self.guess)}')
 
#print(English_Wordle('', 'aback'))
# print(English_Wordle(guess, random))