from check_guess import Check_Guess

class Valid_Input:
    """Checks that user input fulfills all requirements
    """

    def __init__(self, guess):
        """Initializes variables

        Args:
            guess (str): user input
        """
        self.guess = guess
    
    def valid_input(self, guess):
        """Checks that user input fulfills all requirements

        Args:
            guess (str): user input

        Returns:
            boolean or str: If user input fulfills all requirements then True, else returns a message
        """
        self.word = Check_Guess(self.guess)
        # if the length is not 5 and/or all characters aren't letters, the guess is not valid
        if self.word.check_length() == False or self.word.check_for_letters() == False:
            return 'Not a valid guess'
        # guess is not valid if it's not in the word bank
        elif self.word.check_word_bank() == False:
            return 'Word not in word bank'
        else:
            return True