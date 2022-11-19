from english import Get_Random_English
from spanish import Get_Random_Spanish
from wordle import Wordle
from first_word import English_Wordle
from formatting import Formatting
from letters_used import Letters_Used

first_word = Get_Random_English('english.txt')
english_random = first_word.random_word()
print(english_random)

second_word = Get_Random_Spanish('spanish.txt')
spanish_random = second_word.random_word()

guess = ''
first_wordle = Wordle(english_random)
second_wordle = Wordle(spanish_random)
#print(first_wordle)

alphabet = Letters_Used('stare', 'aback')
print(alphabet)