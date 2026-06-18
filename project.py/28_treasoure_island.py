print("welcome to treasoure island Your mission is to find treasure ")
choice_1 = input("where do u want to go ? left or right ").lower()

if choice_1 == "left":
    print("you have reched to lake , there is lake forward .  ")
    choice_2 = input("do u want to swim or wait ?").lower()

    if choice_2 == "wait":
        print("you have reached to the door")

        choice_3 = input("which door you want to enter , red , blue , yellow").lower()
        if choice_3 =="red" :
          print("game over")
        elif choice_3 == "blue" :
          print("game over")
        else:
          print("you win")         
    else:
        print("you have drown into water , game over")
else:
    print("game over")
      
