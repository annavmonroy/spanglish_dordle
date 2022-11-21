from wordle import Wordle
from valid_input import Valid_Input

class Formatting:

    def __init__(self, guess, english_random, spanish_random):
        self.guess = guess
        self.english_random = english_random
        self.spanish_random = spanish_random

    def __str__(self):
        self.num = 1
        self.guess = ''
 
        print('Play Wordle! ')
        # game keeps going until correct answer or runs out of guesses (7)
        while self.num < 8 and (self.guess != self.english_random or self.guess != self.spanish_random):
            self.guess = input(f'Guess {self.num}: ')
            # checks if guess is a valid input
            self.check_input = Valid_Input(self.guess)
            self.check_input = self.check_input.valid_input(self.check_input)
            if self.check_input == True:
                # converts input to uppercase
                self.guess = self.guess.upper()
                self.clues_english = Wordle(self.guess, self.english_random)
                self.clues_spanish = Wordle(self.guess, self.spanish_random)
                print('\tEnglish Word: \tSpanish Word:')
                print('\t   ', self.clues_english.show_colors(self.english_random, self.guess), '\t   ', self.clues_spanish.show_colors(self.spanish_random, self.guess))
                self.num += 1
            else:
                print(self.check_input)

        if self.guess == self.english_random:
            return 'You Win!'
        
        if self.num > 6:
            print('You ran out of guesses')
            return self.english_random