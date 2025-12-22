# TODO-1-Randomly choose a word from the word_list and 
# assign it to a variable called chosen_word. Then print it.

word_list = ["ardvrik", "balloon" , "camel"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)

# Create an empty String called placeholder
# For each letter in the chosen_word, add a to placeholder.

placeholder = ""
word_lenghth = len(chosen_word)
for postion in range(word_lenghth):
    placeholder += "_"
    print(placeholder)

# TODO-2-Ask the user to guess a letter and assign their answer 
# to a variable called guess. Make guess lowercase.
# Use a while loop to let the user guess again.
game_over = False
while not game_over:
    guess = input("guess a letter : ").lower()

# #TODO-3-Check if the letter the user guessed (guess) is one of the letters in the chosen_word. 
# # Print "Right" if it # is Wrong" if it's not.
# So if the chosen_word was "apple", placeholder should be -with 5"" representing each letter 
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"   
print(display)        

# The loop should only stop once the user has guessed all the letters in the chosen_word.
# At that point display has no more blanks ("_"). Then you can tell the user they've won.

if "_" not in display:
    game_over = True
    print("you win")

       
int it at the start of the game.
# TODO-4:
# If the user has entered a letter they've already guessed, print the letter and let them know.
# We should not deduct a life for this.
# e.g. You've already guessed a
# TODO-5:
# If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# song You guessed d, that's not in the word.
# You lose a life.
# TODO-6.
# TODO-6:
# Update the code below to tell the user how many lives they have left.
# print("********
# <???>/6 LIVES
# TODO 7:
# Update the print statement to give the user
# the correct word they were trying to guess.
# e.g. IT WAS <Correct Word> YOU
# LOSE# TODO-1-Randomly choose a word from the word_list and 
# assign it to a variable called chosen_word. Then print it.
# TODO-2-Ask the user to guess a letter and assign their answer 
# to a variable called guess. Make guess lowercase.
# #TODO-3-Check if the letter the user guessed (guess) is one of the letters in the chosen_word. 
# # Print "Right" if it # is Wrong" if it's not.

# Create an empty String called placeholder
# For each letter in the chosen_word, add a to placeholder.
# So if the chosen_word was "apple", placeholder should be -with 5"" representing each letter 

# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word.
# At that point display has no more blanks ("_"). Then you can tell the user they've won.

# Step 4
# Description
# TODO-1:
# Create a variable called lives to keep track of the number of lives left.
# Set lives to equal 6.
# TODO-2:
# If guess is not a letter in the chosen_word, Then reduce lives by 1.
# If lives goes down to then the game should end, and it should print "You lose."
# Hint >
# TODO-3:
# print the ASCII art from the list stages that corresponds to the current number of lives 
# the user has remaining.

# TODO-1:
# Update the word list to use the word_list from hangman_words.py
# TODO-2:
# Update the code to use the stages from the file hangman_art.py
# TODO-3:
# Import the logo from hangman_art.py and pr