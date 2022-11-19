from check_guess import Check_Guess

class Valid_Input:

    def __init__(self, guess):
        self.guess = guess
    
    def valid_input(self, guess):
        self.word = Check_Guess(self.guess)
        if self.word.check_length() == False or self.word.check_for_letters() == False:
            return 'Not a valid guess'
        elif self.word.check_word_bank() == False:
            return 'Word not in word bank'
        else:
            return True