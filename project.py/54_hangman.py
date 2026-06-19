import random

from hangman_words import word_list
from hangman_art import stages , logo


print(logo)


lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
    print(placeholder)


game_over = False
correct_letter = []

while not game_over:

    print(f"************************************** {lives} left ***************************************************")
    guess = input("guess the letter in the word ").lower()


    if guess in correct_letter:
        print(f"you have alredy guessed {guess}")
    
    display = ""

    for letter in chosen_word :
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter :
            display += letter    
        else:
            display += "_"

    print(display) 


    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess} , thats not in the word . You lose a life")

        if lives == 0 :
            game_over = True
            print(f"********************************* YOU LOSS . it was {chosen_word} *********************************************************")

    if "_" not in display :
        game_over = True    
        print("**************************************** You win **********************************************************")   


    print(stages[lives])    