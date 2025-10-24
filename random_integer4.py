import random 

random_integer = random.randint (1 ,10)   #(random..is module && randint is a function)
print(random_integer)


random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_float = random.uniform(1,10)
print(random_float)


# Q. PAUSE 1- Heads or Tails
# Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.
# Hint

random_heads_or_tales = random.randint(0 , 1)
print(random_heads_or_tales)
print("heads")
print("tails")


random_heads_or_tales = random.randint(0 , 1)
if random_heads_or_tales == 0:
    print("heads")
else:
    print("tails")    