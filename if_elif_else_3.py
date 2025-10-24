# if/elif/else
    
#     if condition1:
#         do A
#     elif condition2:
#         do B 
#     else:
#         do this        

print("welcome to rollercoaster")
height = int(input("whats your height in cm?"))

if height >= 120:
    print("you can ride!")
    age = int(input("whats your age ?"))
    if age <= 12:
        print("pay $7.")
    elif age <= 18:  #you can addd asa many elif condition   
        print("pay $12")    
    else:
        print("pay $15.")    
else:
    print("you have to grow taller")


print("welcome to rollercoaster")
height = int(input("whats your height in cm?"))

if height >= 120:
    print("you can ride!")
    age = int(input("whats your age ?"))
    if age <= 12:
        print("pay $7.")
    elif age <= 18:   
        print("pay $12") 
    elif age ==50:
        print("pay $16")      #added one more elif 
    else:
        print("pay $15.")    
else:
    print("you have to grow taller")