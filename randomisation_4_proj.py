game = ["rock" , "paper", "scissors"]
import random 
print("welcome to rock paper scissor game")
user_choice = input("what do u want to chooose ? rock , paper , scissors : ")
computer_choice = random.choice(game)
print(f"computer choice is : {computer_choice}")
print(f"user choice is : {user_choice}")
if user_choice == computer_choice:
    print("its a tie")
elif user_choice == "rock" and computer_choice == "scissors" :
    print("you win")
elif user_choice == "paper" and computer_choice == "rock" :
    print("you win") 
elif user_choice == "scissors" and computer_choice == "paper" :
    print("you win") 
else:
    print("computer wins") 
