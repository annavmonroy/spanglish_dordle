from english import Get_Random_English
from spanish import Get_Random_Spanish
from dordle import Dordle

first_word = Get_Random_English('english.txt')
english_random = first_word.random_word()
print(english_random)

second_word = Get_Random_Spanish('spanish.txt')
spanish_random = second_word.random_word()
print(spanish_random)

guess = ''
word = Dordle(guess, english_random, spanish_random)
print(word)