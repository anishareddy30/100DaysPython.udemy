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
    
       
# TODO-1-Randomly choose a word from the word_list and 
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