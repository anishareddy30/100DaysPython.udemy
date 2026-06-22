import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("guess the letter in te word ").lower()

placeholder = ""


word_length = len(chosen_word)
for length in range (word_length):
    placeholder += "_"
    print(placeholder)


display = ""

game_over = False
correct_letter = []

while not game_over :
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letter.append(guess)
        elif letter in correct_letter :
            display += letter   
        else:
            display += "_"
    print(display)   
    

game_over = True
if guess == chosen_word :
    print("you won ")