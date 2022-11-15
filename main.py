from english import Get_Random_English
from spanish import Get_Random_Spanish
from check_guess import Check_Guess
from first_word import English_Wordle
from second_word import Spanish_Wordle
 
first_word = Get_Random_English('english.txt')
english_random = first_word.random_word()

first_wordle = English_Wordle('', english_random)
print(first_wordle)