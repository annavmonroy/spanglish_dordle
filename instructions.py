class Instructions:
    """Displays instructions for the game
    """

    def __init__(self):
        """Initializes colors
        """
        # ANSI Escape Sequence for color coding and bolding
        self.green = '\x1b[1m\x1b[92m'   #green
        self.yellow = '\x1b[1m\x1b[33m'  #yellow
        self.red = '\x1b[1m\x1b[31m'     #red
        # When finished with a colour need to reset it back to normal text.
        self.reset = '\x1b[0m'          #white

    def display_instructions(self):
        """Displays instructions to the user
        """

        print('\nThe Goal of the game is to guess two 5 letter words at the same time.')
        print('One of the words is in English and the other is in Spanish.')
        print('You have 7 guesses and each guess made counts for both words.\n')

        print('A letter bank will be displayed after every guess where:')
        # adds color to the green, yellow, and red word using ansi escape sequence
        print(f'The letter will turn {self.green}green{self.reset} if it\'s in the word and in the right place')
        print(f'The letter will turn {self.yellow}yellow{self.reset} if it\'s in the word but in the wrong place')
        print(f'The letter will turn {self.red}red{self.reset} if the letter isn\'t in the word')

        print('If you want to exit the game before it\'s over, press Ctrl C')

        print('\nPlay Spanglish Dordle:')