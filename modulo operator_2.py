#MODULO OPERATOR
# it is represented by %(oercentage)
# it is reminder of 2 no
#10 % 5 = 2
#10 % 3 = 3...1 is reminder



# QUESTION
# What do you think this will output?
# print(10 % 3)
# PAUSE 2-Check Odd or Even
# Write some code using what you have learnt about the modulo operator and
# conditional checks in Python to check if the number in he input area is odd or even. 
# If it's odd print out the word "Odd" otherwise printout "Even".

print("check if it is odd or even no ")
number_to_check = int(input("whats the no:" ))

if number_to_check % 2 == 0 :
    print("it is an even no")
else:
    print("it is an odd no")    

