print("welcome to treasure island")
print("your mission to find the treasure")

choice1 = input(' you are at crossroad , where do you want to go ? "left" or "right" ').lower()
if choice1 == "right" :
   choice2 = input('you have come to lake , do u want to wait or swim ? type "wait" to wait for boat or type "swime" ').lower()
   if choice2 == "wait" :
#game will be continue
      choice3 = input('you arrive at the island , which colour do you want to choose ? "red"  "yellow" "blue" ').lower()
      if choice3 == "red" :
         print("room full of fire , game over")
      elif choice3 == "yellow" :
         print("you found the treasore , you win !")
      elif choice3 == "blue" : 
         print("room full of beast , game over!") 
   else:
      print("you got attacked , game is over")
else:
    print("you fall in the hole . game over ")    


