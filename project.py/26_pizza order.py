print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
cost = 0

if size == "S" :
    cost = 15
    print("pay $ 15")
elif size == "M":
    cost = 20
    print("pay $20") 
else :
    cost = 30
    print("pay $30")    

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "y" :
    print("pay $3")
    total = cost + 3 

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "y":
    print("pay $1")
    total_cost = total + 1
    print(f"total bill is {total_cost}")


