from wordle import Wordle
from valid_input import Valid_Input
from display_alphabet import Display_Alphabet
from instructions import Instructions

class Dordle:
    """User Intergface of the game that puts it together into a Dordle
    """

    def __init__(self, guess, english_random, spanish_random):
        """Initializes variables

        Args:
            guess (str): user input
            english_random (str): 5 letter English random word
            spanish_random (str): 5 letter Spanish random word
        """
        self.guess = guess
        self.english_random = english_random
        self.spanish_random = spanish_random

    def __str__(self):
        """Uses several different classes to put the game together into a Dordle and does some formatting

        Returns:
            str: message about winning or lossing
        """
        self.num = 1
        self.guess = ''
        self.check_english = True
        self.check_spanish = True
        self.english_guesses = []
        self.spanish_guesses = []

        # displays instructions to the user
        self.instructions = Instructions()
        self.instructions = self.instructions.display_instructions()

        # game keeps going until correct answer or runs out of guesses (7)
        while self.num < 8 and (self.guess != self.english_random or self.guess != self.spanish_random):
            # displays which guess the user is on and takes the input
            self.guess = input(f'\nGuess {self.num}: ')

            # checks if guess is a valid input
            self.check_input = Valid_Input(self.guess)
            self.check_input = self.check_input.valid_input(self.check_input)
            if self.check_input == True:
                # converts input to uppercase
                self.guess = self.guess.upper()

                # keeps english word running if it hasn't been guessed yet
                if self.check_english == True:
                    # runs the game
                    self.clues_english = Wordle(self.guess, self.english_random)
                    self.english_guesses.append(self.guess)
                    # displays letters used
                    self.english_alphabet = Display_Alphabet(self.english_guesses, self.english_random)
                    self.english_alphabet = self.english_alphabet.check_letters_used(self.english_guesses, self.english_random)

                # keeps spanish word running if it hasn't been guessed yet
                if self.check_spanish == True:
                    # runs the game
                    self.clues_spanish = Wordle(self.guess, self.spanish_random)
                    self.spanish_guesses.append(self.guess)
                    # displays letters used
                    self.spanish_alphabet = Display_Alphabet(self.spanish_guesses, self.spanish_random)
                    self.spanish_alphabet = self.spanish_alphabet.check_letters_used(self.spanish_guesses, self.spanish_random)

                # formatting for user
                print('\tEnglish Word: \tSpanish Word:')
                print('\t   ', self.clues_english.show_colors(self.english_random, self.guess), '\t   ', self.clues_spanish.show_colors(self.spanish_random, self.guess))
                print('English Word:', self.english_alphabet)
                print('Spanish Word:', self.spanish_alphabet)

                # if the word is guess, then the check for the respective language become false
                if self.guess == self.english_random:
                    self.check_english = False
                if self.guess == self.spanish_random:
                    self.check_spanish = False

                # if both checks are false, then the game is over
                if self.check_english == False and self.check_spanish == False:
                    self.english_random = self.spanish_random
                    self.guess = self.english_random

                self.num += 1
            else:
                print(self.check_input)

        # if the word is guessed, the user wins
        if self.guess == self.english_random and self.guess == self.spanish_random:
            return '\nYou Win!'
        
        # if the user runs out of guesses, they lose
        if self.num > 6:
            print('\nYou ran out of guesses')
            return f'English Word: {self.english_random}\nSpanish Word: {self.spanish_random}'