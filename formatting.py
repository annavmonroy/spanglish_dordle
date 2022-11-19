from first_word import English_Wordle

class Formatting:

    def __init__(self, guess, random):
        self.guess = guess
        self.random = random
        self.clues = English_Wordle(self.guess, self.random)

    def __str__(self):
        self.num = 0
        self.guess = None
 
        print('Play Wordle! ')
        # game keeps going until correct answer or runs out of guesses (7)
        while self.num < 6 and self.guess != self.random:
            self.guess = input(f'Guess {self.num}: ')
            # converts input to uppercase
            self.guess = self.guess.upper()
            print(self.clues.check_letters(self.guess, self. random))
            print('\t', self.clues.show_colors(self.random, self.guess))
            self.num += 1

        if self.guess == self.random:
            return 'You Win!'
        
        if self.num > 6:
            print('You ran out of guesses')
            return self.random