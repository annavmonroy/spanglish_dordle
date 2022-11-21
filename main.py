from english import Get_Random_English
from spanish import Get_Random_Spanish
from wordle import Wordle
from dordle import Dordle
from letters_used import Display_Alphabet

first_word = Get_Random_English('english.txt')
english_random = first_word.random_word()
print(english_random)

second_word = Get_Random_Spanish('spanish.txt')
spanish_random = second_word.random_word()
print(spanish_random)

guess = ''
word = Dordle(guess, english_random, spanish_random)
print(word)

alphabet = Display_Alphabet('stare', english_random)
alphabet = alphabet.check_letters_used('stare', english_random)
#print(alphabet)