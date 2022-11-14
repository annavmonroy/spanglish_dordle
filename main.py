from english import Get_Random_English
from spanish import Get_Random_Spanish
from check_guess import Check_Guess
from first_word import English_Wordle
from second_word import Spanish_Wordle
 
guess = str(input('Enter a 5 letter word: '))
 
first_word = Get_Random_English('english.txt')
english_random = first_word.random_word()
 
second_word = Get_Random_Spanish('spanish.txt')
spanish_random = second_word.random_word()
 
correct_input = Check_Guess(guess)
 
if correct_input == True:
    guess = guess.upper()
    first_wordle = English_Wordle(guess, english_random)
    second_wordle = Spanish_Wordle(guess, spanish_random)
    print(first_wordle, second_wordle)
elif correct_input == False:
    print('Invalid input')
else:
    print('Word not in word bank')