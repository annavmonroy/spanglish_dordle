# only checks if guess is a valid input
class Check_Guess:

    def __init_(self, guess, order, lowercase, uppercase):
        self.guess = guess
        self.order = order
        self.lowercase = lowercase
        self.uppercase = uppercase

    def length(self):   # length = 5
        if len(self.guess) != 5:
            raise ValueError('Invalid guess')

    def letters(self):  # no symbols, accent marks, tildes, spaces, etc. # convert everything to uppercase
        for x in range(0, len(self.guess)):
            # converts the value in the string to it's unicode code 
            self.order = ord(self.guess[x])
        self.lowercase = range(97, 122)
        self.uppercase = range(65, 90)

        if self.order not in self.lowercase or self.uppercase:
            raise ValueError('Invalid guess')

    def __str__(self):
        self.guess = self.guess.upper()
        return f'{self.guess}'