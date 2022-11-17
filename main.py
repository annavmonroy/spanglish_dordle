from english import Get_Random_English
from spanish import Get_Random_Spanish
from check_guess import Check_Guess
from first_word import English_Wordle
from second_word import Spanish_Wordle
 
first_word = Get_Random_English('english.txt')
english_random = first_word.random_word()
print(english_random)

second_word = Get_Random_Spanish('spanish.txt')
spanish_random = second_word.random_word()

guess = ''
first_wordle = English_Wordle(guess, english_random)
second_wordle = English_Wordle(guess, spanish_random)
print(first_wordle)