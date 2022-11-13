# import the random word and the guess input
# letters for both words are in a list ex: guess = [a, b, c, d, e]?
class Check_English_Word:

    def __init__(self, guess, random):
        self.guess = guess # replace this with the imported guess input
        self.random = random # replace this with the imported random word
        self.green_letters = []
        self.yellow_letters = []

    def check_green_letters(self):
        for x in range(0, len(self.guess)):
            for y in range(0, len(self.random)):
                if self.guess[x] == self.random[y]:
                    self.green_letters.append(self.guess[x])
    
    def check_yellow_letters(self):
        for x in range(0, len(self.guess)):
            if self.guess[x] in self.random and self.guess[x] not in self.green_letters:
                self.yellow_letters.append(self.guess[x])

# self.guess returned with letters in green, yellow, and white
    def __str__(self):
        pass
