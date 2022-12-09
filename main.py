from english import Get_Random_English
from spanish import Get_Random_Spanish
from dordle import Dordle

# gets random english word
first_word = Get_Random_English('english.txt')
english_random = first_word.random_word()

# gets random spanish word
second_word = Get_Random_Spanish('spanish.txt')
spanish_random = second_word.random_word()

guess = ''
# runs the game, comparing the guess to the english and spanish random words
word = Dordle(guess, english_random, spanish_random)
print(word)