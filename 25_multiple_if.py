height = int(input("whats your height ?"))
bill = 0
if height >= 120 :
    print("can ride")
    age = int(input("whats your age "))
    if age >= 18 :
        bill = 7
        print("pay $7")
    else:
        bill = 10
        print("pay $10") 
    want_photo = (input("do u want photo ? type y or n"))
    if want_photo == "y" :
        bill += 3  
    print(f"total bill is {bill}")       
else:
    print("cant ride")    