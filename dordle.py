from wordle import Wordle
from valid_input import Valid_Input
from display_alphabet import Display_Alphabet

class Dordle:

    def __init__(self, guess, english_random, spanish_random):
        self.guess = guess
        self.english_random = english_random
        self.spanish_random = spanish_random

    def __str__(self):
        self.num = 1
        self.guess = ''
        self.check_english = True
        self.check_spanish = True
 
        print('Play Spanglish Dordle!')

        # game keeps going until correct answer or runs out of guesses (7)
        while self.num < 8 and (self.guess != self.english_random or self.guess != self.spanish_random):
            self.guess = input(f'\nGuess {self.num}: ')

            # checks if guess is a valid input
            self.check_input = Valid_Input(self.guess)
            self.check_input = self.check_input.valid_input(self.check_input)
            if self.check_input == True:
                # converts input to uppercase
                self.guess = self.guess.upper()

                if self.check_english == True:
                    self.clues_english = Wordle(self.guess, self.english_random)
                    self.english_alphabet = Display_Alphabet(self.guess, self.english_random)
                    self.english_alphabet = self.english_alphabet.check_letters_used(self.guess, self.english_random)

                if self.check_spanish == True:
                    self.clues_spanish = Wordle(self.guess, self.spanish_random)
                    self.spanish_alphabet = Display_Alphabet(self.guess, self.spanish_random)
                    self.spanish_alphabet = self.spanish_alphabet.check_letters_used(self.guess, self.spanish_random)

                print('\tEnglish Word: \tSpanish Word:')
                print('\t   ', self.clues_english.show_colors(self.english_random, self.guess), '\t   ', self.clues_spanish.show_colors(self.spanish_random, self.guess))
                print('English Word:', self.english_alphabet)
                print('Spanish Word:', self.spanish_alphabet)

                if self.guess == self.english_random:
                    self.check_english = False
                if self.guess == self.spanish_random:
                    self.check_spanish = False

                if self.check_english == False and self.check_spanish == False:
                    self.english_random = self.spanish_random
                    self.guess = self.english_random

                self.num += 1
            else:
                print(self.check_input)

        if self.guess == self.english_random and self.guess == self.spanish_random:
            return '\nYou Win!'
        
        if self.num > 6:
            print('\nYou ran out of guesses')
            return f'English Word: {self.english_random}\nSpanish Word: {self.spanish_random}'