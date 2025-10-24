#multiple if 
# #if condition1 :
#     do A
# if condition2:
#    do B
# if condition3:
#    do C


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
    else:
        bill = 10
        print("adult ticket is for $10") 

    wants_photo = input("do you want to take photos : ? type y for yes and n for no ")  
    if wants_photo == "y" :
        bill += 3

        print(f"your final bill is {bill}")    

    else:
        print("you are not eligible")       