# Logical operator

# if A and B
#  t and t = t
#  f and f = f
#  t and f = f

# c or d 
#  t or t = t
#  t or f = t
#  f or f = f

# not c
#  not t = f
#  not f = t


# Logical Operators
# Description
# You can combine different conditions using logical operators.
# A and B 
# #Both conditions need to be true C or D 
# #Only one condition needs to be true
# not E #The condition must be false
# PAUSE 1 - Age 45 to 55 Modifier
# Update the code so that people age 45 to 55 (inclusive of both ages) ride for free. 
# Use logical operators to check that the age is greater than 45, and it's also less than 55.



print("welcome to the rollercoaster")
height = int(input("enter your height in cm : "))

if height >= 120 :
    print("you can ride the rollercoaster")
    age = int(input("enter your age : "))
    if age <= 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18 :
        bill = 7
        print("youngster ticket is for $7")
    elif age >= 45 and age <= 55 :  
        print("everything is going to be ok . Have a free ride with us .14") 
    else:
        bill = 10
        print("adult ticket is for $10") 

    wants_photo = input("do you want to take photos : ? type y for yes and n for no ")  
    if wants_photo == "y" :
        bill += 3

        print(f"your final bill is {bill}")    

    else:
        print("you are not eligible")       