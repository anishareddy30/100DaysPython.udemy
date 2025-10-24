# Write a Pizza Delivery Program
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then
#  add up the total for their order and tell them how much they have to pay.
# Small pizza (S): $15
# Medium pizza (M): $20 
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print ("welcome to python pizza")
size = input("what size pizza do you want ? S , M or L")
if size == "S":
  bill = 15
  print("price of small pizza is $15")
elif size == "M":
  bill = 20
  print("price of medium pizza is $20")
elif size == "L" :
  bill = 25
  print("price of large pizza is $25")
else:
  print("you typed the wrong input")  

pepperoni = input("do you want to add pepperoni ? y or n ")
if pepperoni == "y":
  if size == "S":
    bill += 2 
  else :
    bill += 3  

extra_cheese = input("do you want to add extra cheese ? y or n")
if extra_cheese == "y":
  bill += 1

print(f"your final bill is ${bill}") 