# NESTED if

# if condition:
#     if another condition:
#         do this
#     else:
#         do this   
# else:
#     do this

# You can put if/else statements inside other if/else statements. This is known as nesting.

print("welcome to rollercoaster")
height = int(input("whats your height in cm?"))

if height >= 120:
    print("you can ride!")
    age = int(input("whats your age ?"))
    if age <= 18:
        print("pay $7.")
    else:
        print("pay $15.")    
else:
    print("you have to grow taller")


